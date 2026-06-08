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
from ai.offline_generator import generate_question_offline, SUBJECTS, BANKS

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AIProviderManager")

# Carrega o pool de questões seed (gerado pelo ai/generate_seed.py)
_seed_pool: List[Dict[str, Any]] = []
_seed_file = Path(__file__).resolve().parent.parent / "database" / "seed_questions.json"
try:
    if _seed_file.exists():
        with open(_seed_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            _seed_pool = data.get("questions", [])
        logger.info(f"Seed pool carregado: {len(_seed_pool)} questões de {len(SUBJECTS)} assuntos")
    else:
        logger.warning(f"Arquivo seed não encontrado: {_seed_file}. Gere com: python -m ai.generate_seed")
except Exception as e:
    logger.error(f"Erro ao carregar seed pool: {e}")

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
                        "gemini_api_key": cfg.gemini_api_key,
                        "openrouter_api_key": cfg.openrouter_api_key,
                        "deepseek_api_key": cfg.deepseek_api_key,
                        "qwen_api_key": cfg.qwen_api_key,
                        "mistral_api_key": cfg.mistral_api_key,
                        "groq_api_key": cfg.groq_api_key,
                        "temperature": cfg.temperature,
                    }
            finally:
                db.close()
        except Exception as e:
            logger.warning(f"Não foi possível ler SystemConfig: {e}")

        # Variáveis de ambiente sobrescrevem (prioridade máxima)
        env_keys = {
            "active_provider": os.getenv("ACTIVE_PROVIDER"),
            "gemini_api_key": os.getenv("GEMINI_API_KEY"),
            "openrouter_api_key": os.getenv("OPENROUTER_API_KEY"),
            "deepseek_api_key": os.getenv("DEEPSEEK_API_KEY"),
            "qwen_api_key": os.getenv("QWEN_API_KEY"),
            "mistral_api_key": os.getenv("MISTRAL_API_KEY"),
            "groq_api_key": os.getenv("GROQ_API_KEY"),
            "temperature": os.getenv("TEMPERATURE"),
        }

        for k, v in env_keys.items():
            if v is not None:
                if k == "temperature":
                    try:
                        config_from_db[k] = float(v)
                    except ValueError:
                        pass
                else:
                    config_from_db[k] = v

        # Auto-detecção: se alguma chave de IA foi configurada,
        # mas o provider ainda é "offline", ativa o melhor disponível
        # Ordem de preferência: groq (gratuito) > deepseek (barato) > openrouter > gemini > qwen > mistral
        if config_from_db.get("active_provider") == "offline":
            preference = ["groq", "deepseek", "openrouter", "gemini", "qwen", "mistral"]
            for prov in preference:
                if config_from_db.get(f"{prov}_api_key"):
                    config_from_db["active_provider"] = prov
                    logger.info(f"Auto-detecção: provedor ativo definido como '{prov}'")
                    break

        return config_from_db

    @classmethod
    def generate_question(cls, subject: str, bank: str, difficulty: str,
                          db: Any = None, session_id: str = None) -> Dict[str, Any]:
        """Gera questão: alterna entre seed pool, IA e offline para maior variedade"""
        if not bank or bank not in BANKS:
            bank = random.choice(BANKS)
        
        config = cls.get_config()
        provider = config.get("active_provider", "offline")
        has_ai = provider != "offline" and config.get(f"{provider}_api_key")
        
        # 1. Tenta servir do seed pool (com chance de pular se AI disponível para variar)
        use_seed_first = not (has_ai and random.random() < 0.6)
        if use_seed_first:
            seed_q = cls._pick_from_seed_pool(subject, bank, db, session_id)
            if seed_q:
                return seed_q

        # 2. Tenta gerar com IA online
        prompt = cls._build_question_prompt(subject, bank, difficulty)

        all_providers = ["groq", "deepseek", "openrouter", "gemini", "qwen", "mistral"]
        providers_order = [provider] if provider != "offline" else []
        for p in all_providers:
            if p not in providers_order:
                providers_order.append(p)

        for current_prov in providers_order:
            key = config.get(f"{current_prov}_api_key")
            if not key:
                continue
            try:
                logger.info(f"Tentando gerar questão com {current_prov}...")
                question = cls._call_provider(current_prov, key, prompt, config.get("temperature", 0.3))
                if question and isinstance(question, dict):
                    if all(k in question for k in ("enunciado", "gabarito", "options")):
                        question["subject"] = subject
                        question["bank"] = bank
                        if "difficulty" not in question:
                            question["difficulty"] = difficulty
                        logger.info(f"Questão gerada com SUCESSO via {current_prov}")
                        return question
                    logger.warning(f"Resposta do {current_prov} com campos faltando: {list(question.keys())}")
            except Exception as e:
                logger.error(f"Falha com {current_prov}: {e}")

        # 3. Fallback offline dinâmico
        logger.warning("Todos provedores de IA falharam → offline dinâmico")
        return generate_question_offline(subject, bank, difficulty)

    @classmethod
    def _pick_from_seed_pool(cls, subject: str, bank: str,
                              db: Any = None, session_id: str = None) -> Optional[Dict[str, Any]]:
        """Escolhe questão do seed pool, evitando as já respondidas por esta sessão"""
        if not _seed_pool:
            return None

        # Filtra por assunto + banca
        candidates = [q for q in _seed_pool if q["subject"] == subject and q["bank"] == bank]
        if not candidates:
            # Tenta qualquer banca para o assunto
            candidates = [q for q in _seed_pool if q["subject"] == subject]
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
        """Professor Virtual com IA ou fallback offline"""
        config = cls.get_config()
        provider = config.get("active_provider", "offline")

        prompt = (
            f"Você é um Professor de Direito Civil especialista em Direito das Obrigações (arts. 304 a 420 do Código Civil).\n"
            f"Um estudante tem uma dúvida sobre a seguinte questão de prova:\n\n"
            f"Tema: {context.get('subject')}\n"
            f"Banca: {context.get('bank')}\n"
            f"Enunciado: {context.get('enunciado')}\n"
            f"Artigo Relacionado: {context.get('article')}\n"
            f"Fundamentação legal: {context.get('legal_basis')}\n"
            f"Explicação da questão: {context.get('explanation')}\n\n"
            f"Dúvida do estudante: \"{query}\"\n\n"
            f"Responda a dúvida de forma clara, didática, citando a lei correspondente (Código Civil) e explicando o conceito de forma simples."
        )

        providers_order = [provider, "groq", "deepseek", "openrouter", "offline"]
        for current_prov in providers_order:
            if current_prov == "offline":
                return cls._offline_professor_response(context, query)
            key = config.get(f"{current_prov}_api_key")
            if not key:
                continue
            try:
                resp = cls.call_text_provider(current_prov, key, prompt, 0.5)
                if resp:
                    return resp
            except Exception as e:
                logger.error(f"Erro chat Professor com {current_prov}: {e}")

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
            f"Base legal: Código Civil Brasileiro arts. 304 a 420 (Direito das Obrigações).\n"
            f"Formato: CASO CONCRETO com nomes brasileiros fictícios, profissões, valores, cidades e situações cotidianas (compra e venda, locação, financiamento, prestação de serviços).\n\n"
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
            f"Olá! Estou no Modo Offline, mas posso ajudar com base na lei.\n\n"
            f"Esta questão aborda **{context.get('subject')}** e fundamenta-se no **{context.get('article')}**.\n\n"
            f"**Base Legal:**\n\"{context.get('legal_basis')}\"\n\n"
            f"**Explicação:**\n{context.get('explanation')}\n\n"
            f"No Direito das Obrigações (arts. 304 a 420), a literalidade da lei define as regras de pagamento, "
            f"sub-rogação, dação, cláusula penal e arras. Para respostas personalizadas, "
            f"configure uma chave de IA (Gemini ou OpenRouter) no arquivo .env do servidor."
        )
