import sys
import os
import json
import time
import logging
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, Depends, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

from database.connection import Base, engine, get_db, run_migrations
from database.models import SystemConfig, TopicMastery, UserStats, QuestionHistory, ErrorLog, Flashcard
from database.articles_db import ARTICLES_DATA
from ai.manager import AIProviderManager
from services.adaptive import AdaptiveEngine
from services.scheduler import REVISION_INTERVALS
from flashcards.manager import FlashcardManager, FLASHCARD_BANK
from analytics.metrics import AnalyticsMetrics
from reports.generator import ReportGenerator
from backend.session import get_session_id
from ai.offline_generator import generate_question_offline

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("backend")

# Inicializa as tabelas do banco de dados
Base.metadata.create_all(bind=engine)
run_migrations()

app = FastAPI(title="JUS OBRIGAÇÕES MASTER - API Backend")

# CORS: em produção, configure CORS_ORIGINS com os domínios permitidos (separados por vírgula)
cors_origins_env = os.getenv("CORS_ORIGINS", "")
cors_origins = [o.strip() for o in cors_origins_env.split(",") if o.strip()] if cors_origins_env else ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiting simples (em memória)
_rate_limit_store: Dict[str, List[float]] = {}
RATE_LIMIT_REQUESTS = int(os.getenv("RATE_LIMIT_REQUESTS", "60"))
RATE_LIMIT_WINDOW = int(os.getenv("RATE_LIMIT_WINDOW", "60"))

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    if request.url.path.startswith("/api/"):
        client_ip = request.client.host if request.client else "unknown"
        now = time.time()
        window_key = client_ip

        timestamps = _rate_limit_store.get(window_key, [])
        timestamps = [t for t in timestamps if now - t < RATE_LIMIT_WINDOW]
        timestamps.append(now)
        _rate_limit_store[window_key] = timestamps

        if len(timestamps) > RATE_LIMIT_REQUESTS:
            return JSONResponse(
                status_code=429,
                content={"detail": "Muitas requisições. Aguarde e tente novamente."}
            )
    return await call_next(request)



# -------------------------------------------------------------
# PYDANTIC SCHEMAS
# -------------------------------------------------------------
class AnswerPayload(BaseModel):
    question: Dict[str, Any]
    selected_option: str
    response_time: float

class FlashcardReviewPayload(BaseModel):
    is_easy: bool

class ConfigPayload(BaseModel):
    active_provider: str
    gemini_api_key: str
    openrouter_api_key: str
    deepseek_api_key: str
    qwen_api_key: str
    mistral_api_key: str
    groq_api_key: str
    temperature: float

class ProfessorChatPayload(BaseModel):
    context: Dict[str, Any]
    query: str

# -------------------------------------------------------------
# ENDPOINTS API
# -------------------------------------------------------------

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "jus-obrigacoes-master"}

@app.get("/api/dashboard")
def get_dashboard(db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        data = AdaptiveEngine.get_dashboard_data(db, session_id)
        return data
    except Exception:
        logger.exception("Falha ao obter dashboard")
        raise HTTPException(status_code=500, detail="Erro ao obter dados do painel")

@app.get("/api/question/next")
def get_next_question(bank: str = "FGV", subject: Optional[str] = None, db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        if not subject:
            subject = AdaptiveEngine.get_next_subject(db, session_id)
        difficulty = "Médio"
        mastery = db.query(TopicMastery).filter(
            TopicMastery.subject == subject,
            TopicMastery.session_id == session_id
        ).first()
        if mastery:
            if mastery.status == "Critico":
                difficulty = "Fácil"
            elif mastery.status == "Dominado":
                difficulty = "Difícil"
        question = AIProviderManager.generate_question(subject, bank, difficulty, db, session_id)
        return question
    except Exception:
        logger.exception("Falha ao gerar questão")
        raise HTTPException(status_code=500, detail="Erro ao gerar questão")

@app.post("/api/question/answer")
def post_answer(payload: AnswerPayload, db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        # Valida campos obrigatórios da questão
        question = payload.question
        if not question.get("subject"):
            raise HTTPException(status_code=422, detail="Questão inválida: campo 'subject' ausente")
        if not question.get("gabarito"):
            raise HTTPException(status_code=422, detail="Questão inválida: campo 'gabarito' ausente")
        
        existing = db.query(QuestionHistory).filter(
            QuestionHistory.id == str(question.get("id", ""))[:115],
            QuestionHistory.session_id == session_id
        ).first()
        if existing:
            raise HTTPException(status_code=409, detail="Esta questão já foi respondida anteriormente. Carregue uma nova questão.")
        result = AdaptiveEngine.process_answer(
            db, question, payload.selected_option, payload.response_time, session_id
        )
        return result
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Falha ao processar resposta")
        raise HTTPException(status_code=500, detail=f"Erro ao processar resposta: {type(exc).__name__}: {str(exc)[:200]}")

@app.get("/api/flashcards")
def get_flashcards(subject: Optional[str] = None, due_only: bool = False, db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        if subject:
            FlashcardManager.create_cards_for_subject(db, subject, session_id)
            cards = FlashcardManager.get_all_flashcards(db, subject, session_id)
        else:
            if due_only:
                cards = FlashcardManager.get_due_flashcards(db, session_id)
            else:
                for sub in list(FLASHCARD_BANK.keys())[:3]:
                    FlashcardManager.create_cards_for_subject(db, sub, session_id)
                cards = FlashcardManager.get_all_flashcards(db, session_id=session_id)
        return cards
    except Exception:
        logger.exception("Falha ao obter flashcards")
        raise HTTPException(status_code=500, detail="Erro ao obter flashcards")

@app.patch("/api/flashcards/{card_id}/master")
def master_flashcard(card_id: str, db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        card = FlashcardManager.mark_as_mastered(db, card_id, session_id)
        if not card:
            raise HTTPException(status_code=404, detail="Flashcard não encontrado")
        return {"message": "Flashcard marcado como dominado", "next_revision": card.next_revision_date}
    except HTTPException:
        raise
    except Exception:
        logger.exception("Falha ao marcar flashcard como dominado")
        raise HTTPException(status_code=500, detail="Erro ao marcar flashcard como dominado")

@app.post("/api/flashcards/{card_id}/review")
def review_flashcard(card_id: str, payload: FlashcardReviewPayload, db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        card = FlashcardManager.process_review(db, card_id, payload.is_easy, session_id)
        if not card:
            raise HTTPException(status_code=404, detail="Flashcard não encontrado")
        return {"message": "Avaliação salva com sucesso", "next_revision": card.next_revision_date}
    except HTTPException:
        raise
    except Exception:
        logger.exception("Falha ao processar revisão")
        raise HTTPException(status_code=500, detail="Erro ao processar revisão")

@app.get("/api/articles")
def get_articles(query: Optional[str] = None, related: Optional[str] = None):
    try:
        if related:
            subj_map = {str(a["number"]): a["subject"] for a in ARTICLES_DATA}
            subject = subj_map.get(related)
            if not subject:
                for a in ARTICLES_DATA:
                    if related in a["subject"].lower():
                        subject = a["subject"]
                        break
            if subject:
                questions = []
                for bank in ["FGV", "CESPE", "OAB"]:
                    q = generate_question_offline(subject, bank)
                    questions.append(q)
                return {"subject": subject, "questions": questions}
            return {"subject": None, "questions": []}
        if not query:
            return ARTICLES_DATA
        filtered = []
        query_lower = query.lower()
        for art in ARTICLES_DATA:
            if (query_lower in str(art["number"])) or \
               (query_lower in art["subject"].lower()) or \
               (query_lower in art["text"].lower()) or \
               (query_lower in art["summary"].lower()):
                filtered.append(art)
        return filtered
    except Exception:
        logger.exception("Falha ao ler artigos")
        raise HTTPException(status_code=500, detail="Erro ao ler artigos")

@app.get("/api/simulado/start")
def get_simulado(size: int = 10, db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        AdaptiveEngine.initialize_topics_if_needed(db, session_id)
        topics = db.query(TopicMastery).filter(TopicMastery.session_id == session_id).all()
        sorted_topics = sorted(topics, key=lambda x: x.success_rate)
        selected_subjects = [t.subject for t in sorted_topics]
        questions = []
        for i in range(size):
            subj = selected_subjects[i % len(selected_subjects)]
            bank = "FGV" if i % 2 == 0 else "OAB"
            mastery = db.query(TopicMastery).filter(
                TopicMastery.subject == subj,
                TopicMastery.session_id == session_id
            ).first()
            difficulty = "Médio"
            if mastery:
                if mastery.status == "Critico":
                    difficulty = "Fácil"
                elif mastery.status == "Dominado":
                    difficulty = "Difícil"
            q = AIProviderManager.generate_question(subj, bank, difficulty, db, session_id)
            questions.append(q)
        return questions
    except Exception:
        logger.exception("Falha ao iniciar simulado")
        raise HTTPException(status_code=500, detail="Erro ao iniciar simulado")

@app.get("/api/vespera/start")
def get_vespera(db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        return get_simulado(size=50, db=db, session_id=session_id)
    except Exception:
        logger.exception("Falha ao carregar revisão final")
        raise HTTPException(status_code=500, detail="Erro ao carregar revisão final")

@app.get("/api/errors")
def get_error_log(db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        errors = db.query(ErrorLog).filter(
            ErrorLog.resolved == False,
            ErrorLog.session_id == session_id
        ).all()
        result = []
        for err in errors:
            try:
                q_data = json.loads(err.question_json)
            except Exception:
                q_data = {"enunciado": "Erro ao carregar questão", "options": {}, "gabarito": "", "bank": ""}
            result.append({
                "log_id": err.id,
                "subject": err.subject,
                "answered_at": err.answered_at,
                "question": q_data
            })
        return result
    except Exception:
        logger.exception("Falha ao obter log de erros")
        raise HTTPException(status_code=500, detail="Erro ao obter log de erros")

@app.post("/api/errors/train")
def train_errors(db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        errors = db.query(ErrorLog).filter(
            ErrorLog.resolved == False,
            ErrorLog.session_id == session_id
        ).all()
        if not errors:
            return get_simulado(size=5, db=db, session_id=session_id)
        questions = []
        for i, err in enumerate(errors[:10]):
            bank = "OAB" if i % 2 == 0 else "FGV"
            q = AIProviderManager.generate_question(err.subject, bank, "Médio", db, session_id)
            questions.append(q)
        return questions
    except Exception:
        logger.exception("Falha ao criar treino de erros")
        raise HTTPException(status_code=500, detail="Erro ao criar treino de erros")

@app.get("/api/analytics")
def get_analytics(db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        return AnalyticsMetrics.get_advanced_analytics(db, session_id)
    except Exception:
        logger.exception("Falha ao carregar métricas")
        raise HTTPException(status_code=500, detail="Erro ao carregar métricas")

@app.get("/api/report")
def get_cognitive_report(db: Session = Depends(get_db), session_id: str = Depends(get_session_id)):
    try:
        return ReportGenerator.generate_cognitive_report(db, session_id)
    except Exception:
        logger.exception("Falha ao processar relatório")
        raise HTTPException(status_code=500, detail="Erro ao processar relatório")

@app.get("/api/config")
def get_config():
    cfg = AIProviderManager.get_config()
    env_providers = []
    for p in ["gemini", "openrouter", "deepseek", "qwen", "mistral"]:
        if os.getenv(f"{p.upper()}_API_KEY"):
            env_providers.append(p)
    cfg["env_providers"] = env_providers
    for key_name in ["gemini_api_key", "openrouter_api_key", "deepseek_api_key", "qwen_api_key", "mistral_api_key", "groq_api_key"]:
        if key_name in cfg and cfg[key_name]:
            val = cfg[key_name]
            if len(val) > 12:
                cfg[key_name] = val[:4] + "*" * (len(val) - 8) + val[-4:]
    return cfg

@app.post("/api/config")
def post_config(payload: ConfigPayload, db: Session = Depends(get_db)):
    try:
        config = db.query(SystemConfig).first()
        if not config:
            config = SystemConfig()
            db.add(config)
        config.active_provider = payload.active_provider
        config.gemini_api_key = payload.gemini_api_key
        config.openrouter_api_key = payload.openrouter_api_key
        config.deepseek_api_key = payload.deepseek_api_key
        config.qwen_api_key = payload.qwen_api_key
        config.mistral_api_key = payload.mistral_api_key
        config.groq_api_key = payload.groq_api_key
        config.temperature = payload.temperature
        db.commit()
        return {"message": "Configurações salvas com sucesso"}
    except Exception:
        logger.exception("Falha ao salvar configurações")
        raise HTTPException(status_code=500, detail="Erro ao salvar configurações")

@app.post("/api/ai/professor/chat")
def chat_with_professor(payload: ProfessorChatPayload):
    try:
        response = AIProviderManager.ask_professor(payload.context, payload.query)
        return {"response": response}
    except Exception:
        logger.exception("Falha no chat com o professor")
        raise HTTPException(status_code=500, detail="Erro no chat com o professor")


# -------------------------------------------------------------
# SPA: serve o frontend buildado (se existir) para rotas não-API
# -------------------------------------------------------------
FRONTEND_DIST = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend", "dist")
if os.path.isdir(FRONTEND_DIST):
    app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIST, "assets")), name="assets")
    logger.info("Frontend build encontrado. Servindo arquivos estáticos de %s", FRONTEND_DIST)

    from fastapi.responses import FileResponse

    @app.exception_handler(404)
    async def spa_404(request: Request, exc):
        if request.url.path.startswith("/api/") or request.url.path.startswith("/health") or request.url.path.startswith("/assets/"):
            return JSONResponse({"detail": "Not found"}, status_code=404)
        index_path = os.path.join(FRONTEND_DIST, "index.html")
        if os.path.isfile(index_path):
            return FileResponse(index_path)
        return JSONResponse({"detail": "Not found"}, status_code=404)
