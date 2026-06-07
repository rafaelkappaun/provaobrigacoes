from datetime import datetime, timedelta, timezone
import json
import logging
import os
import random
from typing import Dict, Any, List, Optional
from sqlalchemy.orm import Session
from database.models import TopicMastery, UserStats, QuestionHistory, ErrorLog, Flashcard
from ai.offline_generator import SUBJECTS
from ai.manager import AIProviderManager

logger = logging.getLogger("AdaptiveEngine")

# Limite para considerar acerto inseguro (em segundos)
INSECURE_TIME_LIMIT = 45.0

class AdaptiveEngine:
    @staticmethod
    def initialize_topics_if_needed(db: Session, session_id: str = "default"):
        """Inicializa todos os 23 assuntos no banco de dados se vazios"""
        for subject in SUBJECTS:
            mastery = db.query(TopicMastery).filter(
                TopicMastery.subject == subject,
                TopicMastery.session_id == session_id
            ).first()
            if not mastery:
                mastery = TopicMastery(
                    session_id=session_id,
                    subject=subject,
                    questions_answered=0,
                    questions_correct=0,
                    consecutive_errors=0,
                    consecutive_correct=0,
                    success_rate=0.0,
                    status="Critico",
                    ease_factor=2.5,
                    interval_days=0,
                    next_revision_date=datetime.now(timezone.utc).replace(tzinfo=None)
                )
                db.add(mastery)
        
        # Inicializa stats globais
        stats = db.query(UserStats).filter(UserStats.session_id == session_id).first()
        if not stats:
            stats = UserStats(
                session_id=session_id,
                total_time_seconds=0,
                questions_answered=0,
                questions_correct=0,
                streak_days=0,
                last_study_date=None
            )
            db.add(stats)
            
        db.commit()

    @classmethod
    def get_dashboard_data(cls, db: Session, session_id: str = "default") -> Dict[str, Any]:
        """Obtém todas as métricas para a tela inicial"""
        cls.initialize_topics_if_needed(db, session_id)
        
        stats = db.query(UserStats).filter(UserStats.session_id == session_id).first()
        if not stats:
            logger.warning("UserStats not found for session %s, creating inline", session_id)
            stats = UserStats(
                session_id=session_id,
                total_time_seconds=0,
                questions_answered=0,
                questions_correct=0,
                streak_days=0,
                last_study_date=None
            )
            db.add(stats)
            db.flush()
        
        topics = db.query(TopicMastery).filter(TopicMastery.session_id == session_id).all()
        
        total_answered = stats.questions_answered
        total_correct = stats.questions_correct
        overall_success_rate = (total_correct / total_answered * 100.0) if total_answered > 0 else 0.0
        
        # Conta tópicos por status
        criticos = sum(1 for t in topics if t.status == "Critico")
        intermediarios = sum(1 for t in topics if t.status == "Intermediario")
        dominados = sum(1 for t in topics if t.status == "Dominado")
        
        # Verifica se existe algum tema em Modo Intensivo
        intensive_subject = None
        for t in topics:
            if t.consecutive_errors >= 3:
                intensive_subject = t.subject
                break
                
        # Detalhamento de cada assunto
        subjects_detail = []
        for t in topics:
            subjects_detail.append({
                "subject": t.subject,
                "questions_answered": t.questions_answered,
                "questions_correct": t.questions_correct,
                "success_rate": round(t.success_rate, 1),
                "status": t.status,
                "consecutive_errors": t.consecutive_errors,
                "consecutive_correct": t.consecutive_correct,
                "mastery_target": "5/5",
                "is_intensive": t.consecutive_errors >= 3
            })
            
        # Ranking pessoal (faixa)
        if total_answered >= 100:
            ranking = "Mestre em Obrigações"
            ranking_emoji = "👑"
        elif total_answered >= 50:
            ranking = "Jurista Expert"
            ranking_emoji = "🏆"
        elif total_answered >= 25:
            ranking = "Estudante Avançado"
            ranking_emoji = "🥇"
        elif total_answered >= 10:
            ranking = "Aprendiz Dedicado"
            ranking_emoji = "🥈"
        elif total_answered >= 5:
            ranking = "Iniciante"
            ranking_emoji = "🥉"
        else:
            ranking = "Novato"
            ranking_emoji = "🌱"
            
        # Próximo passo: orientação inteligente
        meta_achieved_flag = overall_success_rate >= 95.0 and total_answered >= 50
        next_step = "Continue praticando para atingir 95% de acertos em todos os temas."
        if total_answered == 0:
            next_step = "🌟 Responda sua primeira questão para começar sua jornada!"
        else:
            env_keys = ["GROQ_API_KEY", "DEEPSEEK_API_KEY", "OPENROUTER_API_KEY", "GEMINI_API_KEY"]
            has_ai_key = any(os.getenv(k) for k in env_keys)
            if not has_ai_key:
                ai_status = AIProviderManager.get_config()
                has_any_key = any(ai_status.get(f"{p}_api_key") for p in ["groq", "deepseek", "openrouter", "gemini", "qwen", "mistral"])
                if not has_any_key:
                    next_step = "🔑 Configure uma chave de IA gratuita (Groq) no arquivo .env para gerar questões ilimitadas personalizadas."
            if meta_achieved_flag or overall_success_rate >= 95:
                next_step = "🏆 Meta 95% atingida! Faça um simulado completo para fixar o conhecimento."
            elif intensive_subject:
                next_step = f"🔥 Modo Intensivo ativo em '{intensive_subject}'. Estude este tema para desbloquear os demais."
            elif criticos > 0:
                criticos_names = [t.subject for t in topics if t.status == "Critico"][:3]
                next_step = f"🎯 Foco total nos temas críticos: {', '.join(criticos_names)}. Pratique até atingir 60%."
            elif intermediarios > 0:
                next_step = f"📈 Você está evoluindo! Reforce {intermediarios} temas intermediários para chegar ao domínio total."
            elif dominados == len(topics) and dominados > 0:
                next_step = "💪 Domínio total! Você já domina todos os temas. Tente o modo simulado para se desafiar ainda mais."

        return {
            "overall_success_rate": round(overall_success_rate, 1),
            "questions_answered": total_answered,
            "questions_correct": total_correct,
            "total_time_seconds": stats.total_time_seconds,
            "streak_days": stats.streak_days,
            "meta_achieved": overall_success_rate >= 95.0 and total_answered >= 50,
            "meta_progress": round(min(100, overall_success_rate / 95.0 * 100), 1) if total_answered > 0 else 0,
            "ranking": ranking,
            "ranking_emoji": ranking_emoji,
            "criticos_count": criticos,
            "intermediarios_count": intermediarios,
            "dominados_count": dominados,
            "intensive_subject": intensive_subject,
            "subjects": subjects_detail,
            "next_step": next_step
        }

    @classmethod
    def process_answer(cls, db: Session, question: Dict[str, Any], selected_option: str, response_time: float, session_id: str = "default") -> Dict[str, Any]:
        """Processa a resposta do aluno e atualiza o mecanismo adaptativo"""
        cls.initialize_topics_if_needed(db, session_id)
        
        subject = question["subject"]
        correct_option = question["gabarito"]
        is_correct = (selected_option.upper() == correct_option.upper())
        is_insecure = is_correct and (response_time > INSECURE_TIME_LIMIT)
        
        # 1. Registrar histórico
        q_history = QuestionHistory(
            id=question["id"],
            session_id=session_id,
            subject=subject,
            difficulty=question.get("difficulty", "Médio"),
            bank=question.get("bank", "FGV"),
            is_correct=is_correct,
            response_time=response_time,
            is_insecure=is_insecure
        )
        db.add(q_history)
        
        # 2. Atualizar estatísticas globais
        stats = db.query(UserStats).filter(UserStats.session_id == session_id).first()
        if not stats:
            stats = UserStats(session_id=session_id, total_time_seconds=0, questions_answered=0, questions_correct=0, streak_days=0)
            db.add(stats)
            db.flush()
        stats.questions_answered += 1
        if is_correct:
            stats.questions_correct += 1
            
        stats.total_time_seconds += int(response_time)
        
        # Lógica de streak (sequência)
        today = datetime.now(timezone.utc).replace(tzinfo=None).date()
        if stats.last_study_date:
            last_date = stats.last_study_date.date()
            if today == last_date:
                pass # mesmo dia, mantém
            elif today == last_date + timedelta(days=1):
                stats.streak_days += 1
            else:
                stats.streak_days = 1
        else:
            stats.streak_days = 1
        stats.last_study_date = datetime.now(timezone.utc).replace(tzinfo=None)
        
        # 3. Atualizar domínio do assunto (TopicMastery)
        mastery = db.query(TopicMastery).filter(
            TopicMastery.subject == subject,
            TopicMastery.session_id == session_id
        ).first()
        if not mastery:
            mastery = TopicMastery(session_id=session_id, subject=subject, questions_answered=0, questions_correct=0, consecutive_errors=0, success_rate=0.0, status="Critico")
            db.add(mastery)
            db.flush()
        mastery.questions_answered += 1
        
        # Se for um acerto em Modo Intensivo, ou erro, tratamos consecutividade
        was_intensive = (mastery.consecutive_errors >= 3)
        
        if is_correct:
            mastery.questions_correct += 1
            mastery.consecutive_correct += 1
            
            if was_intensive:
                # Modo Intensivo: reduz erros gradualmente conforme acerta
                mastery.consecutive_errors = max(0, mastery.consecutive_errors - 1)
            else:
                mastery.consecutive_errors = 0
            
            # 5 acertos consecutivos = Domínio total (saída do intensivo)
            if mastery.consecutive_correct >= 5:
                mastery.status = "Dominado"
                mastery.consecutive_errors = 0
        else:
            # Erro: zera os acertos consecutivos, precisa recomeçar
            mastery.consecutive_correct = 0
            mastery.consecutive_errors += 1
            
            # Salvar no log de erros
            import hashlib
            error_id = hashlib.md5(f"{question['id']}_{session_id}_{datetime.now(timezone.utc).replace(tzinfo=None).timestamp()}".encode()).hexdigest()[:40]
            error_log = ErrorLog(
                id=error_id,
                session_id=session_id,
                subject=subject,
                question_json=json.dumps(question, ensure_ascii=False),
                resolved=False
            )
            db.add(error_log)
            
        # Recalcula taxa de sucesso do assunto (apenas para referência)
        mastery.success_rate = (mastery.questions_correct / mastery.questions_answered) * 100.0
        
        # Atualiza Status (se ainda não dominou por consecutivos)
        if mastery.status != "Dominado":
            if mastery.success_rate < 60.0:
                mastery.status = "Critico"
            elif mastery.success_rate < 85.0:
                mastery.status = "Intermediario"
            elif mastery.consecutive_correct >= 5:
                mastery.status = "Dominado"
            else:
                mastery.status = "Intermediario"
            
        # 4. Agendamento de Repetição Espaçada
        from services.scheduler import SpacedRepetitionScheduler
        SpacedRepetitionScheduler.schedule_next_revision(mastery, is_correct, is_insecure)
        
        db.commit()
        
        # 5. Lógica de feedback do Professor Particular
        feedback = cls._generate_professor_feedback(question, selected_option, is_correct, is_insecure)
        
        # 6. Reforço Automático (gerado em caso de erro normal)
        reinforcement = None
        new_intensive_triggered = (mastery.consecutive_errors == 3 and not was_intensive)
        
        if not is_correct:
            if new_intensive_triggered:
                # Dispara Modo Intensivo especial
                reinforcement = cls._generate_intensive_payload(subject)
            else:
                # Dispara Reforço Automático normal
                reinforcement = cls._generate_reinforcement_payload(subject, question)
                
        return {
            "is_correct": is_correct,
            "is_insecure": is_insecure,
            "feedback": feedback,
            "new_intensive_triggered": new_intensive_triggered,
            "reinforcement": reinforcement,
            "topic_status": mastery.status,
            "topic_success_rate": round(mastery.success_rate, 1)
        }

    @classmethod
    def get_next_subject(cls, db: Session, session_id: str = "default") -> str:
        """Determina o próximo assunto — distribuição igualitária entre não-dominados"""
        cls.initialize_topics_if_needed(db, session_id)
        
        topics = db.query(TopicMastery).filter(TopicMastery.session_id == session_id).all()
        
        # 1. Modo Intensivo: assunto com 3+ erros consecutivos
        for t in topics:
            if t.consecutive_errors >= 3:
                logger.info(f"Modo Intensivo Ativo para: {t.subject}")
                return t.subject
        
        # 2. Separa dominados (consecutive_correct >= 5) e não-dominados
        mastered = [t for t in topics if t.consecutive_correct >= 5]
        not_mastered = [t for t in topics if t.consecutive_correct < 5]
        
        if not not_mastered:
            return random.choice(topics).subject
        
        # 3. Distribuição igualitária: peso inverso ao total de perguntas respondidas
        #    Quanto menos respondeu, maior a chance de ser selecionado
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        
        weights = []
        for t in not_mastered:
            weight = 1.0 / (t.questions_answered + 1)
            if t.next_revision_date and t.next_revision_date <= now:
                weight *= 3
            weights.append(weight)
        
        total = sum(weights)
        if total > 0:
            normalized = [w / total for w in weights]
            chosen = random.choices(not_mastered, weights=normalized, k=1)[0]
            return chosen.subject
        
        return random.choice(not_mastered).subject

    @staticmethod
    def _generate_professor_feedback(question: Dict[str, Any], selected_option: str, is_correct: bool, is_insecure: bool) -> Dict[str, Any]:
        """Gera a mensagem do Professor com base na resposta do aluno"""
        subject = question["subject"]
        article = question.get("article", "Código Civil")
        legal_basis = question.get("legal_basis", "")
        explanation = question.get("explanation", "")
        
        if is_correct:
            title = "✅ EXCELENTE! VOCÊ ACERTOU!"
            if is_insecure:
                title = "⚠️ ACERTO INSEGURO! (Você demorou mais de 45 segundos)"
                
            intro = f"Você marcou a alternativa **{selected_option}** e ela é a CORRETA, em conformidade com o **{article}**."
            body = (
                f"**Fundamentação Legal:**\n> \"{legal_basis}\"\n\n"
                f"**Raciocínio Didático:**\n{explanation}\n\n"
                f"Continue mantendo essa linha de raciocínio! Fique atento às sutilezas dos termos da lei."
            )
        else:
            title = "❌ REVISÃO NECESSÁRIA! VOCÊ ERROU!"
            intro = f"Você marcou a alternativa **{selected_option}**, mas o gabarito oficial é a alternativa **{question['gabarito']}**."
            body = (
                f"**Onde ocorreu o erro?**\nPara resolver este caso concreto de **{subject}**, era indispensável lembrar do **{article}**.\n\n"
                f"**O que diz a lei?**\n> \"{legal_basis}\"\n\n"
                f"**Análise da Questão:**\n{explanation}\n\n"
                f"**Dica do Professor:** Não confunda os conceitos. O adimplemento das obrigações exige atenção a quem paga, a quem se paga e os prazos."
            )
            
        return {
            "title": title,
            "intro": intro,
            "body": body,
            "article": article,
            "legal_basis": legal_basis
        }

    @staticmethod
    def _generate_reinforcement_payload(subject: str, question: Dict[str, Any]) -> Dict[str, Any]:
        """Gera resumos em 3 níveis (30s, 2min, 5min), 3 flashcards e mapa mental rico"""
        article = question.get("article", "Código Civil")
        legal_basis = question.get("legal_basis", "Artigo correspondente")
        explanation = question.get("explanation", "")
        
        # Resumo 30s (ultra conciso)
        summary_30s = (
            f"**Resumo de 30s: {subject}**\n\n"
            f"📍 **Conceito:** {subject} regula como as obrigações são quitadas ou descumpridas.\n"
            f"📌 **Artigo-chave:** {article}\n"
            f"⚡ **Pegadinha comum:** {legal_basis[:100]}..."
        )
        
        # Resumo 2min (mais completo)
        summary_2min = (
            f"**Resumo de 2 minutos: {subject}**\n\n"
            f"**O que é?**\n"
            f"No Direito das Obrigações (CC/02), {subject.lower()} trata das regras específicas "
            f"que regem o adimplemento ou inadimplemento das prestações entre credor e devedor.\n\n"
            f"**Base legal:** {article}\n"
            f"\"{legal_basis[:200]}...\"\n\n"
            f"**Como cai em prova?**\n"
            f"As bancas (FGV, CESPE, OAB) exploram este tema através de casos concretos com "
            f"pegadinhas nos detalhes: prazos, quem pode pagar, lugar do pagamento, exceções legais.\n\n"
            f"**Dica do professor:** Leia o artigo com atenção redobrada aos parágrafos e incisos."
        )
        
        # Resumo 5min (completo, com jurisprudencia e doutrina)
        summary_5min = (
            f"**Resumo de 5 minutos: {subject}**\n\n"
            f"**1. CONCEITO DOUTRINÁRIO**\n"
            f"{subject} é um dos pilares do Direito das Obrigações. A doutrina clássica (Caio Mário, "
            f"Pontes de Miranda, Orlando Gomes) ensina que o adimplemento é a realização voluntária "
            f"da prestação devida, enquanto o inadimplemento é o seu descumprimento total ou parcial.\n\n"
            f"**2. FUNDAMENTAÇÃO LEGAL**\n"
            f"Artigo principal: {article}\n"
            f"Texto integral: \"{legal_basis}\"\n\n"
            f"**3. JURISPRUDÊNCIA APLICÁVEL**\n"
            f"O STJ consolidou o entendimento de que a boa-fé objetiva (art. 422, CC) deve nortear "
            f"as relações obrigacionais, vedando comportamentos contraditórios (venire contra factum proprium).\n\n"
            f"**4. ANÁLISE DO CASO CONCRETO**\n"
            f"{explanation[:300]}...\n\n"
            f"**5. PONTOS DE PROVA (MAIS COBRADOS)**\n"
            f"• Distinção entre mora e inadimplemento absoluto\n"
            f"• Efeitos do pagamento por terceiro (interessado vs não interessado)\n"
            f"• Sub-rogação legal vs convencional\n"
            f"• Novação objetiva vs subjetiva\n"
            f"• Cláusula penal compensatória vs moratória\n"
            f"• Arras confirmatórias vs penitenciais"
        )
        
        # 3 Flashcards
        flashcards = [
            {
                "front": f"Qual o principal artigo do CC que disciplina o tema '{subject}'?",
                "back": f"É o {article}. Cujo teor expressa: \"{legal_basis[:120]}...\""
            },
            {
                "front": f"No caso concreto da questão, qual seria a conduta juridicamente correta?",
                "back": f"A conduta correta é o cumprimento exato da obrigação conforme o {article}."
            },
            {
                "front": f"Por que a alternativa que você marcou na questão de '{subject}' estava incorreta?",
                "back": f"Porque contrariava a regra expressa de que o pagamento deve observar quem é o legítimo receptor/devedor."
            }
        ]
        
        # Mapa Mental Textual Rico
        mind_map = (
            f"🧠 MAPA MENTAL: {subject.upper()}\n"
            f"{'═' * 50}\n\n"
            f"┌─ DIREITO DAS OBRIGAÇÕES (CC 304-420)\n"
            f"│\n"
            f"├──► {subject.upper()}\n"
            f"│      │\n"
            f"│      ├──► Artigos: {article}\n"
            f"│      │\n"
            f"│      ├──► Requisitos Essenciais\n"
            f"│      │      ├─ Capacidade das partes\n"
            f"│      │      ├─ Objeto lícito e possível\n"
            f"│      │      └─ Forma prescrita/defesa em lei\n"
            f"│      │\n"
            f"│      ├──► Efeitos Jurídicos\n"
            f"│      │      ├─ Adimplemento → Extinção\n"
            f"│      │      ├─ Mora → Juros + correção\n"
            f"│      │      └─ Inadimplemento → Perdas e danos\n"
            f"│      │\n"
            f"│      ├──► Pegadinhas de Prova\n"
            f"│      │      ├─ Confundir sub-rogação com novação\n"
            f"│      │      ├─ Achar que credor aceita pagamento diverso\n"
            f"│      │      └─ Ignorar exceções legais (arts. 373, 399)\n"
            f"│      │\n"
            f"│      └──► Conexões com outros temas\n"
            f"│             ├─ Adimplemento → Pagamento, Dação, Novação\n"
            f"│             └─ Inadimplemento → Mora, Perdas, Cláusula Penal\n"
            f"│\n"
            f"└──► Fonte: Código Civil Brasileiro de 2002\n"
            f"        Arts. 304 a 420"
        )
        
        return {
            "type": "reforco_normal",
            "summary_30s": summary_30s,
            "summary_2min": summary_2min,
            "summary_5min": summary_5min,
            "flashcards": flashcards,
            "mind_map": mind_map
        }

    @staticmethod
    def _generate_intensive_payload(subject: str) -> Dict[str, Any]:
        """Gera o material do Modo Intensivo (Errou o mesmo tema 3 vezes) com 10 questões inéditas"""
        from ai.offline_generator import SUBJECTS, BANKS, generate_question_offline
        
        # Resumo Completo
        summary = (
            f"🔥 **MODO INTENSIVO ATIVADO: {subject.upper()}** 🔥\n\n"
            f"Você apresentou dificuldades recorrentes em **{subject}** (3 erros consecutivos).\n"
            f"A partir de agora, novos assuntos foram bloqueados temporariamente. Vamos dominar este tema juntos!\n\n"
            f"**CONCEITO COMPLETO:**\n"
            f"O Direito Civil brasileiro estabelece regras muito claras sobre este instituto nos artigos 304 a 420. "
            f"No caso de {subject}, a doutrina majoritária e a jurisprudência entendem que o cumprimento deve ser "
            f"integral, de boa-fé e conforme as obrigações acessórias pactuadas. O descumprimento gera mora ou inadimplemento absoluto."
        )
        
        # Jurisprudência
        jurisprudence = (
            f"⚖️ **JURISPRUDÊNCIA RELEVANTE:**\n"
            f"\"O adimplemento da obrigação deve observar os ditames da boa-fé objetiva (Art. 422, CC). A conduta contraditória "
            f"do credor ou devedor (venire contra factum proprium) atrai a caracterização de mora ou inadimplemento culposo, "
            f"gerando o dever de indenizar via cláusula penal ou perdas e danos.\" (STJ, REsp adaptado)."
        )
        
        # 10 Flashcards
        flashcards = [
            {"front": f"O que é essencial observar em {subject}?", "back": f"Os artigos aplicáveis do Código Civil (arts. 304 a 420)."},
            {"front": f"Quem é o sujeito passivo da relação de pagamento em {subject}?", "back": "O devedor, embora terceiros possam pagar."},
            {"front": f"O credor é obrigado a aceitar prestação diversa em {subject}?", "back": "Não, ainda que mais valiosa (Art. 313)."},
            {"front": f"A mora pressupõe culpa em {subject}?", "back": "Sim, exceto se a lei dispuser de outra forma (Art. 396)."},
            {"front": f"O que acontece com as garantias na novação de {subject}?", "back": "Extinguem-se se o fiador não anuir (Art. 364)."},
            {"front": f"As perdas e danos incluem lucros cessantes em {subject}?", "back": "Sim, além do que efetivamente perdeu (Art. 402)."},
            {"front": f"Qual a taxa dos juros legais em {subject} se não convencionados?", "back": "Segundo a taxa em vigor para impostos da Fazenda Nacional (Art. 406)."},
            {"front": f"Qual o limite do valor da cláusula penal em {subject}?", "back": "Não pode exceder o valor da obrigação principal (Art. 412)."},
            {"front": f"Arras confirmatórias permitem indenização suplementar?", "back": "Sim, se provado maior prejuízo (Art. 419)."},
            {"front": f"Arras penitenciais permitem indenização suplementar?", "back": "Não, servem como indenização máxima (Art. 420)."}
        ]
        
        # 10 questões inéditas do assunto
        intensive_questions = []
        banks_for_intensive = ["FGV", "CESPE", "OAB", "FCC", "VUNESP"]
        for i in range(10):
            bank = banks_for_intensive[i % len(banks_for_intensive)]
            q = generate_question_offline(subject, bank)
            intensive_questions.append(q)
        
        return {
            "type": "modo_intensivo",
            "summary": summary,
            "jurisprudence": jurisprudence,
            "flashcards": flashcards,
            "intensive_questions": intensive_questions,
            "message": "Você precisa obter pelo menos 80% de acertos nas próximas 10 questões deste tema para desbloquear o sistema."
        }
