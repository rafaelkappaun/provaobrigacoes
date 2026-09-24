import os
import json
import re
import random
import httpx
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv
from database.connection import SessionLocal
from database.models import SystemConfig
from database.crypto import decrypt_value
from ai.offline_generator import generate_question_offline, SUBJECTS, BANKS
from ai.multiportas_generator import generate_multiportas_question_offline, MULTIPORTAS_SUBJECTS

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AIProviderManager")

# 1. Carrega o pool de questões seed de Contratos
_seed_pool: List[Dict[str, Any]] = []
_seed_file = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"
try:
    if _seed_file.exists():
        with open(_seed_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            _seed_pool = data.get("questions", [])
        logger.info(f"Seed pool Contratos carregado: {len(_seed_pool)} questões de {len(SUBJECTS)} assuntos")
except Exception as e:
    logger.error(f"Erro ao carregar seed pool Contratos: {e}")

# 2. Carrega o pool de questões seed de Modelo Multiportas
_multiportas_seed_pool: List[Dict[str, Any]] = []
_multiportas_file = Path(__file__).resolve().parent.parent / "database" / "seed_multiportas.json"
try:
    if _multiportas_file.exists():
        with open(_multiportas_file, "r", encoding="utf-8") as f:
            m_data = json.load(f)
            _multiportas_seed_pool = m_data.get("questions", [])
        logger.info(f"Seed pool Multiportas carregado: {len(_multiportas_seed_pool)} questões de {len(MULTIPORTAS_SUBJECTS)} assuntos")
except Exception as e:
    logger.error(f"Erro ao carregar seed pool Multiportas: {e}")

class AIProviderManager:
    @staticmethod
    def get_config() -> Dict[str, Any]:
        """Obtém configuração priorizando variáveis de ambiente (.env), depois banco de dados"""
        config_from_db = {"active_provider": "offline", "temperature": 0.3}
        
        try:
            db = SessionLocal()
            try:
                cfg = db.query(SystemConfig).first()
                if cfg:
                    config_from_db = {
                        "active_provider": cfg.active_provider,
                        "gemini_api_key": decrypt_value(cfg.gemini_api_key),
                        "openrouter_api_key": decrypt_value(cfg.openrouter_api_key),
                        "deepseek_api_key": decrypt_value(cfg.deepseek_api_key),
                        "qwen_api_key": decrypt_value(cfg.qwen_api_key),
                        "mistral_api_key": decrypt_value(cfg.mistral_api_key),
                        "groq_api_key": decrypt_value(cfg.groq_api_key),
                        "temperature": cfg.temperature,
                    }
            finally:
                db.close()
        except Exception as e:
            logger.warning(f"Não foi possível ler SystemConfig: {e}")

        return config_from_db

    @classmethod
    def generate_question(cls, subject: str, bank: str, difficulty: str,
                          db: Any = None, session_id: str = None, module: str = "contratos") -> Dict[str, Any]:
        """Gera questão 100% offline: isolada por módulo (contratos ou multiportas)"""
        if not bank or bank not in BANKS:
            bank = random.choice(BANKS)
            
        if module == "multiportas":
            if not subject or subject not in MULTIPORTAS_SUBJECTS:
                subject = random.choice(MULTIPORTAS_SUBJECTS)
            seed_q = cls._pick_from_seed_pool(subject, bank, db, session_id, pool=_multiportas_seed_pool)
            if seed_q:
                return dict(seed_q)
            if _multiportas_seed_pool:
                candidates = [q for q in _multiportas_seed_pool if q.get("subject") == subject]
                if candidates:
                    q = dict(random.choice(candidates))
                    q["id"] = f"{q.get('id', 'multi')}_{random.randint(1000, 9999)}"
                    return q
            return generate_multiportas_question_offline(subject, bank, difficulty)
            
        # Padrão: módulo de contratos
        if not subject or subject not in SUBJECTS:
            subject = random.choice(SUBJECTS)
            
        # 1. Tenta servir do seed pool (prioriza não respondidas na sessão)
        seed_q = cls._pick_from_seed_pool(subject, bank, db, session_id, pool=_seed_pool)
        if seed_q:
            return dict(seed_q)

        # 2. Se já respondeu todas as sementes daquele assunto, reaproveita do seed pool com ID novo
        if _seed_pool:
            candidates = [q for q in _seed_pool if q.get("subject") == subject]
            if candidates:
                q = dict(random.choice(candidates))
                q["id"] = f"{q.get('id', 'seed')}_{random.randint(1000, 9999)}"
                return q

        # 3. Fallback: gerador procedural offline dinâmico
        return generate_question_offline(subject, bank, difficulty)

    @classmethod
    def _pick_from_seed_pool(cls, subject: str, bank: str,
                              db: Any = None, session_id: str = None,
                              pool: Optional[List[Dict[str, Any]]] = None) -> Optional[Dict[str, Any]]:
        """Escolhe questão do seed pool do respectivo módulo, evitando as já respondidas por esta sessão"""
        active_pool = pool if pool is not None else _seed_pool
        if not active_pool:
            return None

        # Filtra por assunto + banca
        candidates = [q for q in active_pool if q["subject"] == subject and q["bank"] == bank]
        if not candidates:
            # Tenta qualquer banca para o assunto
            candidates = [q for q in active_pool if q["subject"] == subject]
        if not candidates:
            return None

        # Se temos db/session, filtra já respondidas por esta sessão usando question_id
        if db is not None and session_id is not None and candidates:
            from database.models import QuestionHistory
            candidate_ids = [q["id"] for q in candidates]
            # Busca pelo campo question_id (novo) ou por id que começa com o question_id (legado)
            try:
                answered_qids = set(
                    row[0] for row in db.query(QuestionHistory.question_id)
                    .filter(QuestionHistory.session_id == session_id)
                    .filter(QuestionHistory.question_id.in_(candidate_ids))
                    .all()
                    if row[0]
                )
            except Exception:
                answered_qids = set()
            candidates = [q for q in candidates if q["id"] not in answered_qids]

        if not candidates:
            return None

        # Deduplica por texto das alternativas para evitar questões com opções idênticas
        opt_groups: dict = {}
        for q in candidates:
            opt_key = json.dumps(q.get("options", {}), sort_keys=True)
            opt_groups.setdefault(opt_key, []).append(q)
        group = random.choice(list(opt_groups.values()))
        q = random.choice(group)

        # Se temos db/session, evita conteúdo similar já respondido nesta sessão
        if db is not None and session_id is not None:
            try:
                from database.models import QuestionHistory
                answered = db.query(QuestionHistory.question_json).filter(
                    QuestionHistory.session_id == session_id,
                    QuestionHistory.question_json.isnot(None)
                ).all()
                answered_opts = set()
                for row in answered:
                    try:
                        qj = json.loads(row[0]) if isinstance(row[0], str) else row[0]
                        if qj and "options" in qj:
                            answered_opts.add(json.dumps(qj["options"], sort_keys=True))
                    except Exception:
                        pass
                if json.dumps(q.get("options", {}), sort_keys=True) in answered_opts:
                    remaining = [g for g in opt_groups if g not in answered_opts]
                    if remaining:
                        group = opt_groups[random.choice(remaining)]
                        q = random.choice(group)
            except Exception:
                pass

        logger.info(f"Seed pool: questão {q['id'][:8]} para {subject}/{bank}")
        return q

    @classmethod
    def ask_professor(cls, context: Dict[str, Any], query: str) -> str:
        """Professor Virtual 100% offline com fundamentação direta na lei"""
        return cls._offline_professor_response(context, query)

    @staticmethod
    def _build_question_prompt(subject: str, bank: str, difficulty: str) -> str:
        is_cespe = bank == "CESPE"
        options_format = (
            "A: CERTO e B: ERRADO (apenas uma correta)" if is_cespe
            else "A, B, C, D e E (apenas uma correta)"
        )
        alt_keys = '{"A": "Alternativa A", "B": "Alternativa B", ...}' if not is_cespe else '{"A": "CERTO", "B": "ERRADO"}'

        return (
            f"Gere uma questão inédita no estilo da banca {bank}, assunto '{subject}', dificuldade '{difficulty}'.\n"
            f"Base legal: Código Civil Brasileiro (Direito dos Contratos, Escada Ponteana arts. 104 a 114, Teoria Geral arts. 421 a 480, vícios redibitórios e figuras afins).\n"
            f"Formato: CASO CONCRETO com nomes brasileiros fictícios, profissões, valores, cidades e situações práticas contratuais.\n\n"
            f"Retorne APENAS JSON válido, sem markdown:\n"
            f"{{\n"
            f'  "id": "q_<uuid>",\n'
            f'  "subject": "{subject}",\n'
            f'  "bank": "{bank}",\n'
            f'  "difficulty": "{difficulty}",\n'
            f'  "enunciado": "Caso concreto longo e detalhado...",\n'
            f'  "options": {alt_keys},\n'
            f'  "gabarito": "Letra correta (ex: C)",\n'
            f'  "article": "Art. XXX do Código Civil",\n'
            f'  "legal_basis": "Texto do artigo que resolve o caso.",\n'
            f'  "explanation": "Explicação didática: por que a correta está certa e por que as demais (pegadinhas) estão erradas."\n'
            f"}}\n\n"
            f"Formato das alternativas: {options_format}."
        )

    @staticmethod
    def _parse_json_response(text: str) -> Optional[Dict[str, Any]]:
        """Extrai e parseia JSON da resposta, removendo markdown se necessário"""
        if not text:
            return None
        text = text.strip()

        # Remove blocos de código markdown
        if text.startswith("`"):
            match = re.search(r"```(?:json)?\s*([\s\S]*?)```", text)
            if match:
                text = match.group(1).strip()

        # Tenta parse direto
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

        # Tenta extrair primeiro { ... } completo
        brace_match = re.search(r"\{[\s\S]*\}", text)
        if brace_match:
            try:
                return json.loads(brace_match.group(0))
            except json.JSONDecodeError:
                pass

        logger.error(f"Não foi possível fazer parse do JSON. Texto: {text[:200]}...")
        return None

    @classmethod
    def _call_provider(cls, provider: str, api_key: str, prompt: str, temperature: float) -> Optional[Dict[str, Any]]:
        """Chama API e retorna dict ou None"""
        url, headers, payload = cls._build_request(provider, api_key, prompt, temperature, json_mode=True)

        try:
            with httpx.Client(timeout=45.0) as client:
                response = client.post(url, headers=headers, json=payload)
                if response.status_code != 200:
                    logger.error(f"Erro HTTP {response.status_code} do {provider}: {response.text[:300]}")
                    return None

                resp_json = response.json()
                text = ""

                if provider == "gemini":
                    candidates = resp_json.get("candidates", [])
                    if candidates:
                        text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                else:
                    choices = resp_json.get("choices", [])
                    if choices:
                        text = choices[0].get("message", {}).get("content", "")

                if not text:
                    logger.warning(f"Resposta vazia do {provider}")
                    return None

                return cls._parse_json_response(text)

        except httpx.TimeoutException:
            logger.error(f"Timeout ao chamar {provider}")
            return None
        except Exception as e:
            logger.error(f"Erro inesperado ao chamar {provider}: {e}")
            return None

    @classmethod
    def call_text_provider(cls, provider: str, api_key: str, prompt: str, temperature: float) -> Optional[str]:
        """Chama API para resposta textual"""
        url, headers, payload = cls._build_request(provider, api_key, prompt, temperature, json_mode=False)

        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.post(url, headers=headers, json=payload)
                if response.status_code != 200:
                    return None

                resp_json = response.json()
                if provider == "gemini":
                    candidates = resp_json.get("candidates", [])
                    if candidates:
                        return candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                else:
                    choices = resp_json.get("choices", [])
                    if choices:
                        return choices[0].get("message", {}).get("content", "")
                return None
        except Exception:
            return None

    @staticmethod
    def _build_request(provider: str, api_key: str, prompt: str, temperature: float, json_mode: bool):
        """Constrói a requisição HTTP para cada provedor"""
        if provider == "gemini":
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
            headers = {"Content-Type": "application/json"}
            gen_config = {"temperature": temperature}
            if json_mode:
                gen_config["responseMimeType"] = "application/json"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": gen_config,
            }
            return url, headers, payload

        if provider == "openrouter":
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://jusobrigacoesmaster.app",
                "X-Title": "Jus Obrigacoes Master",
            }
            payload = {
                "model": "google/gemini-2.0-flash-001",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature,
            }
            if json_mode:
                payload["response_format"] = {"type": "json_object"}
            return url, headers, payload

        if provider == "groq":
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
            payload = {
                "model": "llama-3.3-70b-versatile",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature,
                "max_tokens": 2048,
            }
            if json_mode:
                payload["response_format"] = {"type": "json_object"}
            return url, headers, payload

        if provider == "deepseek":
            url = "https://api.deepseek.com/v1/chat/completions"
            headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature,
            }
            if json_mode:
                payload["response_format"] = {"type": "json_object"}
            return url, headers, payload

        # qwen / mistral → OpenRouter
        model_map = {
            "qwen": "qwen/qwen-2.5-72b-instruct",
            "mistral": "mistralai/mistral-7b-instruct",
        }
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://jusobrigacoesmaster.app",
            "X-Title": "Jus Obrigacoes Master",
        }
        payload = {
            "model": model_map.get(provider, "google/gemini-2.0-flash-001"),
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
        }
        return url, headers, payload

    @staticmethod
    def _offline_professor_response(context: Dict[str, Any], query: str) -> str:
        return (
            f"Olá! Segue a fundamentação jurídica desta questão:\n\n"
            f"• **Assunto:** {context.get('subject')}\n"
            f"• **Dispositivo Legal:** {context.get('article')}\n\n"
            f"**Texto da Lei (Código Civil):**\n\"{context.get('legal_basis')}\"\n\n"
            f"**Análise da Questão:**\n{context.get('explanation')}\n\n"
            f"💡 **Dica de Estudo:** Para fixar este conteúdo e alcançar 90% de acertos, memorize a redação do {context.get('article')} e preste atenção aos requisitos e prazos legais."
        )
