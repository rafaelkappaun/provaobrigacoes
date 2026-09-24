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

    @staticmethod
    def _shuffle_and_balance_question(question: Dict[str, Any]) -> Dict[str, Any]:
        """
        Embaralha uniformemente as alternativas (A, B, C, D) e recalcula o gabarito.
        Garante que a resposta correta tenha probabilidade idêntica (25%) em cada letra (A, B, C, D),
        eliminando qualquer vício na alternativa A ou na primeira posição.
        """
        if not question or "options" not in question or "gabarito" not in question:
            return question

        q = dict(question)
        options = dict(q.get("options", {}))
        current_gabarito = str(q.get("gabarito", "")).strip().upper()

        if not options or current_gabarito not in options:
            return q

        correct_text = options[current_gabarito]
        texts = list(options.values())
        random.shuffle(texts)

        letters = ["A", "B", "C", "D", "E"][:len(texts)]
        shuffled_options = {}
        new_gabarito = current_gabarito

        for letter, text in zip(letters, texts):
            shuffled_options[letter] = text
            if text == correct_text:
                new_gabarito = letter

        q["options"] = shuffled_options
        q["gabarito"] = new_gabarito
        return q

    @classmethod
    def generate_question(cls, subject: str, bank: str, difficulty: str,
                          db: Any = None, session_id: str = None, module: str = "contratos") -> Dict[str, Any]:
        """Gera questão 100% offline: isolada por módulo (contratos ou multiportas), sem repetição de questões já respondidas"""
        if not bank or bank not in BANKS:
            bank = random.choice(BANKS)
            
        if module == "multiportas":
            if not subject or subject not in MULTIPORTAS_SUBJECTS:
                subject = random.choice(MULTIPORTAS_SUBJECTS)
            
            # 1. Tenta servir do seed pool para o assunto solicitado (evitando já respondidas na sessão)
            seed_q = cls._pick_from_seed_pool(subject, bank, db, session_id, pool=_multiportas_seed_pool)
            if seed_q:
                return cls._shuffle_and_balance_question(dict(seed_q))
                
            # 2. Se já respondeu todas as sementes deste assunto, busca outros assuntos de Multiportas com questões pendentes
            other_subjects = [s for s in MULTIPORTAS_SUBJECTS if s != subject]
            random.shuffle(other_subjects)
            for alt_subj in other_subjects:
                alt_q = cls._pick_from_seed_pool(alt_subj, bank, db, session_id, pool=_multiportas_seed_pool)
                if alt_q:
                    logger.info(f"Multiportas: assunto '{subject}' esgotado na sessão. Redirecionando para '{alt_subj}'.")
                    return cls._shuffle_and_balance_question(dict(alt_q))
            
            # 3. Se TODOS os 14 assuntos e 56 sementes foram respondidos na sessão, gera procedural inédito
            logger.info("Multiportas: todas as sementes da sessão esgotadas. Gerando procedural inédito.")
            return cls._shuffle_and_balance_question(generate_multiportas_question_offline(subject, bank, difficulty))
            
        # Padrão: módulo de contratos
        if not subject or subject not in SUBJECTS:
            subject = random.choice(SUBJECTS)
            
        # 1. Tenta servir do seed pool (prioriza não respondidas na sessão)
        seed_q = cls._pick_from_seed_pool(subject, bank, db, session_id, pool=_seed_pool)
        if seed_q:
            return cls._shuffle_and_balance_question(dict(seed_q))

        # 2. Se já respondeu todas as sementes deste assunto, busca outros assuntos de Contratos com questões pendentes
        other_subjects = [s for s in SUBJECTS if s != subject]
        random.shuffle(other_subjects)
        for alt_subj in other_subjects:
            alt_q = cls._pick_from_seed_pool(alt_subj, bank, db, session_id, pool=_seed_pool)
            if alt_q:
                logger.info(f"Contratos: assunto '{subject}' esgotado na sessão. Redirecionando para '{alt_subj}'.")
                return cls._shuffle_and_balance_question(dict(alt_q))

        # 3. Fallback: gerador procedural offline dinâmico
        logger.info("Contratos: todas as sementes da sessão esgotadas. Gerando procedural inédito.")
        return cls._shuffle_and_balance_question(generate_question_offline(subject, bank, difficulty))

    @classmethod
    def _pick_from_seed_pool(cls, subject: str, bank: str,
                              db: Any = None, session_id: str = None,
                              pool: Optional[List[Dict[str, Any]]] = None) -> Optional[Dict[str, Any]]:
        """Escolhe questão do seed pool do respectivo módulo, garantindo que TODAS as questões não respondidas sejam aproveitadas"""
        active_pool = pool if pool is not None else _seed_pool
        if not active_pool:
            return None

        # 1. Pega todas as questões do assunto no pool
        subject_candidates = [q for q in active_pool if q.get("subject") == subject]
        if not subject_candidates:
            return None

        # 2. Se temos db/session, filtra rigorosamente as já respondidas por esta sessão
        if db is not None and session_id is not None:
            from database.models import QuestionHistory
            try:
                history_rows = db.query(QuestionHistory.question_id, QuestionHistory.id).filter(
                    QuestionHistory.session_id == session_id
                ).all()
                answered_ids = set()
                session_suffix = f"_{session_id[:20]}"
                for qid, hid in history_rows:
                    if qid:
                        clean_qid = str(qid).strip()
                        answered_ids.add(clean_qid)
                        if "_" in clean_qid:
                            answered_ids.add(clean_qid.rsplit("_", 1)[0])
                    if hid:
                        clean_hid = str(hid).strip()
                        answered_ids.add(clean_hid)
                        if session_suffix in clean_hid:
                            base_hid = clean_hid.split(session_suffix)[0]
                            answered_ids.add(base_hid)
                            if "_" in base_hid:
                                answered_ids.add(base_hid.rsplit("_", 1)[0])
                
                # Exclui qualquer questão do assunto que já tenha sido respondida
                unanswered = [
                    q for q in subject_candidates 
                    if q["id"] not in answered_ids and not any(q["id"] == aid or q["id"].startswith(aid) for aid in answered_ids)
                ]
            except Exception as e:
                logger.warning(f"Erro ao verificar histórico de questões respondidas: {e}")
                unanswered = subject_candidates
        else:
            unanswered = subject_candidates

        if not unanswered:
            return None

        # 3. Entre as NÃO respondidas, dá preferência à banca solicitada se houver; senão, aceita qualquer banca do assunto
        bank_matches = [q for q in unanswered if q.get("bank") == bank]
        candidates_to_pick = bank_matches if bank_matches else unanswered

        q = random.choice(candidates_to_pick)
        logger.info(f"Seed pool: questão {q['id']} selecionada para '{subject}' (banca {q.get('bank')}, restam {len(unanswered)} no assunto)")
        return dict(q)

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
