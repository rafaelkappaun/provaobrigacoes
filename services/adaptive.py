from datetime import datetime, timedelta, timezone
import hashlib
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

import math

# Limite para considerar acerto inseguro (em segundos)
INSECURE_TIME_LIMIT = 45.0

TOPIC_STUDY_GUIDE: Dict[str, Dict[str, str]] = {
    "Planos do Negócio Jurídico (Escada Ponteana)": {
        "articles": "Arts. 104, 166 e 171 do Código Civil",
        "key_concept": "Teoria de Pontes de Miranda: 1) Existência (agente, vontade, objeto e forma); 2) Validade (capacidade, vontade livre, objeto lícito/possível, forma prescrita/não defesa); 3) Eficácia (condição, termo e encargo).",
        "trap": "Incapacidade ou ilicitude gera nulidade/anulabilidade no plano da validade. O negócio existe no mundo fático, mas é inválido."
    },
    "Princípios do Direito Contratual": {
        "articles": "Arts. 421 e 421-A do Código Civil (Lei da Liberdade Econômica)",
        "key_concept": "Contratos civis e empresariais presumem-se paritários e simétricos. Prevalecem a autonomia privada, a intervenção mínima judicial e a observância estrita da alocação de riscos acordada pelas partes.",
        "trap": "A função social do contrato não autoriza o juiz a reescrever cláusulas livremente ajustadas entre partes capazes."
    },
    "Boa-fé Objetiva e Figuras Parcelares": {
        "articles": "Arts. 113, 187 e 422 do Código Civil",
        "key_concept": "Padrão de lealdade e eticidade nas fases pré, durante e pós-contratual. Figuras: Venire contra factum proprium (vedação a comportamento contraditório), Supressio (perda de direito pela inércia), Surrectio (nascimento de prerrogativa pelo costume), Tu quoque e Duty to mitigate.",
        "trap": "Aceitar pagamentos sem ressalvas em data diversa durante longo período gera Supressio, impedindo cobrança retroativa de encargos."
    },
    "Interpretação dos Contratos no Direito Brasileiro": {
        "articles": "Arts. 112 e 113 do Código Civil",
        "key_concept": "Nas declarações de vontade atender-se-á mais à intenção comum das partes do que ao sentido estrito e literal da linguagem. Devem ser interpretados conforme a boa-fé e os usos do lugar da celebração.",
        "trap": "Em contratos de adesão, cláusulas ambíguas ou contraditórias devem ser interpretadas a favor do aderente (contra proferentem)."
    },
    "Classificação dos Contratos": {
        "articles": "Teoria Geral dos Contratos (Código Civil)",
        "key_concept": "Unilaterais (obrigação para apenas uma parte) vs. Bilaterais (obrigações recíprocas/sinalagma). Gratuitos vs. Onerosos. Comutativos (prestações certas) vs. Aleatórios (álea/risco).",
        "trap": "Todo contrato é bilateral na sua formação (exige duas partes), mas pode ser classificado como unilateral quanto aos seus efeitos obrigacionais (ex: doação pura)."
    },
    "Etapas de Formação do Contrato": {
        "articles": "Arts. 427 a 435 do Código Civil",
        "key_concept": "Fases: 1) Negociações preliminares (puntuação); 2) Proposta/Policitação (vinculante, salvo as exceções do art. 428); 3) Aceitação tempestiva; 4) Conclusão. Contrato entre ausentes aperfeiçoa-se pela teoria da expedição.",
        "trap": "Lugar da celebração: considera-se celebrado o contrato no lugar em que foi proposto (art. 435 CC)."
    },
    "Estipulação em Favor de Terceiro": {
        "articles": "Arts. 436 a 438 do Código Civil",
        "key_concept": "O estipulante pode exigir o cumprimento da obrigação a favor do terceiro, e o terceiro também pode exigi-la. O estipulante pode substituir o terceiro a qualquer momento por ato inter vivos ou testamento.",
        "trap": "Se ao terceiro for deixado o direito de reclamar a execução, o estipulante não pode exonerar o devedor sem a concordância expressa do terceiro."
    },
    "Promessa de Fato de Terceiro": {
        "articles": "Arts. 439 e 440 do Código Civil",
        "key_concept": "Aquele que tiver prometido fato de terceiro responderá por perdas e danos se o terceiro não cumprir. Se o terceiro aceitar a obrigação perante o credor, o promitente original fica totalmente exonerado.",
        "trap": "A obrigação não existirá se o terceiro for cônjuge do promitente nas hipóteses previstas em lei."
    },
    "Contratos Aleatórios - Conceito e Espécies": {
        "articles": "Arts. 458 a 461 do Código Civil",
        "key_concept": "Contratos em que a prestação de uma das partes depende de evento futuro e incerto (álea deliberada). Dividem-se em álea sobre coisas futuras (emptio spei e emptio rei speratae) e álea sobre coisas existentes expostas a risco.",
        "trap": "Sem a assunção de risco voluntária pelas partes não há contrato aleatório, mas sim negócio comutativo sujeito às regras ordinárias."
    },
    "Contrato Aleatório: Emptio Spei": {
        "articles": "Art. 458 do Código Civil",
        "key_concept": "Alienação da esperança: o risco assumido pelo adquirente é sobre a própria existência da coisa. O alienante tem direito ao preço total mesmo que nada venha a existir, desde que não tenha havido dolo ou culpa.",
        "trap": "Exemplo da rede jogada ao mar: o adquirente paga o valor total combinado mesmo se vier completamente vazia."
    },
    "Contrato Aleatório: Emptio Rei Speratae": {
        "articles": "Art. 459 do Código Civil",
        "key_concept": "Alienação da coisa esperada: o risco assumido é sobre a quantidade da coisa. O alienante terá direito ao preço integral desde que qualquer quantidade venha a existir. Se NADA vier a existir, o contrato é ineficaz e o preço não é devido.",
        "trap": "Diferença vital: no Emptio Spei o preço é devido mesmo com zero de colheita; no Emptio Rei Speratae deve existir ao menos uma quantidade mínima."
    },
    "Contrato Aleatório: Coisas Existentes Expostas a Risco": {
        "articles": "Arts. 460 e 461 do Código Civil",
        "key_concept": "Refere-se a coisas existentes, mas sujeitas a risco assumido pelo adquirente. O alienante terá direito a todo o preço mesmo que a coisa já não existisse no todo ou em parte na data do negócio.",
        "trap": "O negócio é anulável por dolo se o alienante já sabia da consumação do risco (ex: perda da mercadoria em alto-mar antes da venda)."
    },
    "Contrato Preliminar / Promessa de Contratar": {
        "articles": "Arts. 462 a 466 do Código Civil",
        "key_concept": "O contrato preliminar deve conter todos os requisitos essenciais do contrato a ser celebrado, exceto a forma. Permite execução específica perante o Judiciário para suprir a vontade da parte recalcitrante.",
        "trap": "A forma pública (ex: escritura) não é obrigatória no pré-contrato, ainda que o contrato definitivo dependa dela por lei."
    },
    "Contrato com Pessoa a Declarar": {
        "articles": "Arts. 467 a 471 do Código Civil",
        "key_concept": "Cláusula pro amico: faculdade concedida a uma parte de indicar terceiro que assumirá seus direitos e obrigações. Prazo legal de indicação: 5 dias. A indicação deve obedecer à mesma forma do contrato originário.",
        "trap": "A aceitação do terceiro opera com eficácia retroativa ex tunc (desde o momento da celebração original)."
    },
    "Contrato com Pessoa a Declarar vs. Outros Contratos": {
        "articles": "Arts. 467 a 471 do CC vs. Cessão e Mandato",
        "key_concept": "Com a nomeação válida, o contratante originário sai totalmente da relação. Se a pessoa indicada for incapaz ou insolvente ao tempo da nomeação, o contrato produz efeitos entre os signatários originais.",
        "trap": "Diferente da cessão de contrato (que opera ex nunc) e do mandato (onde o mandatário age desde o início em nome alheio)."
    },
    "Vícios Redibitórios - Conceito e Requisitos": {
        "articles": "Arts. 441 e 442 do Código Civil",
        "key_concept": "Defeito oculto pré-existente à tradição em contrato comutativo ou doação onerosa que torne a coisa imprópria ao uso a que se destina ou diminua sensivelmente seu valor. Não se aplica a doação pura.",
        "trap": "O defeito deve ser oculto e pré-existente. Defeitos aparentes ou surgidos após a entrega não geram redibição civil."
    },
    "Efeitos da Boa-fé e Má-fé do Alienante no Vício": {
        "articles": "Art. 443 do Código Civil",
        "key_concept": "Se o alienante conhecia o vício (má-fé): restitui o valor recebido + perdas e danos. Se não conhecia o vício (boa-fé): restitui apenas o valor recebido + despesas contratuais.",
        "trap": "A responsabilidade civil do alienante subsiste mesmo se a coisa perecer em poder do adquirente, caso o perecimento decorra do vício oculto (art. 444)."
    },
    "Ações Edilícias (Redibitória e Estimatória/Quanti Minoris)": {
        "articles": "Arts. 441 e 442 do Código Civil",
        "key_concept": "Opções exclusivas do adquirente: 1) Ação Redibitória: rescindir o contrato e reaver o valor pago; OU 2) Ação Estimatória (Quanti Minoris): conservar a coisa e pleitear abatimento proporcional no preço.",
        "trap": "As ações edilícias são alternativas e excludentes: o autor não pode cumular redibição com abatimento pelo mesmo defeito."
    },
    "Vício Redibitório vs. Entrega de Coisa Diversa (Aliud Pro Alio)": {
        "articles": "Art. 441 CC vs. Arts. 389 e 205 do Código Civil",
        "key_concept": "No vício redibitório entrega-se a coisa contratada com defeito funcional oculto (prazo decadencial curto). No aliud pro alio entrega-se coisa substancialmente diferente da pactuada (inadimplemento contratual com prazo prescricional decenal).",
        "trap": "Entregar sementes de espécie botânica distinta da comprada é aliud pro alio (inadimplemento), sujeito a prazo prescricional geral de 10 anos."
    },
    "Prazos Decadenciais dos Vícios Redibitórios": {
        "articles": "Arts. 445 e 446 do Código Civil",
        "key_concept": "Regra geral contada da tradição: 30 dias para bens móveis e 1 ano para imóveis. Se o vício só puder ser conhecido mais tarde: prazo móvel é de 180 dias e imóvel de 1 ano para o vício aparecer; contam-se então 30 dias (móveis) ou 1 ano (imóveis) da ciência.",
        "trap": "A garantia contratual suspende a contagem legal, mas o adquirente deve denunciar o defeito ao alienante nos 30 dias seguintes ao descobrimento sob pena de decadência."
    },
    "Extinção dos Contratos - Resolução e Cláusula Resolutiva": {
        "articles": "Arts. 474 e 475 do Código Civil",
        "key_concept": "A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial. A parte prejudicada pelo inadimplemento pode pedir a resolução ou exigir o cumprimento, cabendo sempre indenização por perdas e danos.",
        "trap": "A resolução decorre do descumprimento culposo ou fortuito; difere da resilição (unilateral/denúncia ou bilateral/distrato) e da rescisão."
    },
    "Exceção do Contrato Não Cumprido e Onerosidade Excessiva": {
        "articles": "Arts. 476 a 480 do Código Civil",
        "key_concept": "Exceptio non adimpleti contractus (art. 476): nenhum contratante pode exigir a prestação do outro sem antes ter cumprido a sua. Onerosidade excessiva (art. 478): resolução em contratos de execução continuada/diferida por evento extraordinário e imprevisível.",
        "trap": "A resolução por onerosidade excessiva pode ser evitada se a parte contrária oferecer modificação equitativa das condições contratuais (art. 479)."
    }
}

class AdaptiveEngine:
    @staticmethod
    def initialize_topics_if_needed(db: Session, session_id: str = "default"):
        """Inicializa todos os 22 assuntos de Contratos no banco de dados se vazios e limpa legados"""
        # Remove tópicos legados que não pertençam aos 22 temas do questionário
        db.query(TopicMastery).filter(
            TopicMastery.session_id == session_id,
            ~TopicMastery.subject.in_(SUBJECTS)
        ).delete(synchronize_session=False)

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
        """Obtém todas as métricas com foco na Meta de 90% de acertos e recomendações de estudo"""
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
        
        # Detalhamento de cada assunto com cálculo para meta 90%
        subjects_detail = []
        study_recommendations = []
        
        for t in topics:
            guide = TOPIC_STUDY_GUIDE.get(t.subject, {
                "articles": "Código Civil Brasileiro",
                "key_concept": f"Revisar o conceito e principais requisitos legais de {t.subject}.",
                "trap": "Atenção aos prazos legais e exceções expressas na lei."
            })
            
            is_goal_achieved = (t.questions_answered >= 3 and t.success_rate >= 90.0)
            
            # Cálculo de acertos necessários para atingir 90%:
            # (correct + x) / (answered + x) >= 0.9 => 0.1x >= 0.9*answered - correct
            if is_goal_achieved:
                needed_for_90 = 0
            elif t.questions_answered == 0:
                needed_for_90 = 3
            else:
                raw_needed = (0.9 * t.questions_answered - t.questions_correct) / 0.1
                needed_for_90 = max(1, min(15, math.ceil(raw_needed)))
                
            # Status pedagógico claro
            if t.questions_answered == 0:
                display_status = "NaoIniciado"
            elif is_goal_achieved:
                display_status = "Dominado"
            elif t.success_rate >= 70.0:
                display_status = "Intermediario"
            else:
                display_status = "Critico"
                
            sub_info = {
                "subject": t.subject,
                "questions_answered": t.questions_answered,
                "questions_correct": t.questions_correct,
                "questions_incorrect": t.questions_answered - t.questions_correct,
                "success_rate": round(t.success_rate, 1),
                "status": display_status,
                "consecutive_errors": t.consecutive_errors,
                "consecutive_correct": t.consecutive_correct,
                "is_goal_achieved": is_goal_achieved,
                "needed_for_90": needed_for_90,
                "articles": guide["articles"],
                "key_concept": guide["key_concept"],
                "trap": guide["trap"]
            }
            subjects_detail.append(sub_info)
            
            # Se ainda não atingiu a meta de 90%, entra na lista de recomendações de estudo
            if not is_goal_achieved:
                # Prioridade: menor taxa de acerto primeiro; depois os com mais erros
                priority_score = (100.0 - t.success_rate) + (20 if t.questions_answered > 0 else 0)
                study_recommendations.append({
                    **sub_info,
                    "priority_score": priority_score
                })

        # Ordena recomendações: maior prioridade primeiro
        study_recommendations.sort(key=lambda x: x["priority_score"], reverse=True)
        # Remove campo de cálculo interno
        for rec in study_recommendations:
            rec.pop("priority_score", None)

        # Contagem por status
        dominados_count = sum(1 for s in subjects_detail if s["is_goal_achieved"])
        criticos_count = sum(1 for s in subjects_detail if s["status"] == "Critico")
        intermediarios_count = sum(1 for s in subjects_detail if s["status"] == "Intermediario")
        nao_iniciados_count = sum(1 for s in subjects_detail if s["status"] == "NaoIniciado")
            
        # Ranking pessoal
        if total_answered >= 100 and overall_success_rate >= 80:
            ranking = "Mestre em Contratos"
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
        elif total_answered >= 3:
            ranking = "Iniciante"
            ranking_emoji = "🥉"
        else:
            ranking = "Novato"
            ranking_emoji = "🌱"
            
        # Orientação pedagógica direta para a Meta de 90%
        meta_achieved_flag = overall_success_rate >= 90.0 and total_answered >= 30 and dominados_count >= 15
        if total_answered == 0:
            next_step = "🌟 Responda sua primeira questão para iniciar seu diagnóstico rumo aos 90%!"
        elif meta_achieved_flag:
            next_step = "🏆 Parabéns! Você atingiu a Meta de 90% de acertos nos conteúdos de Contratos!"
        elif study_recommendations:
            top_rec = study_recommendations[0]
            if top_rec["questions_answered"] == 0:
                next_step = f"📖 Inicie os estudos de '{top_rec['subject']}' ({top_rec['articles']}) para cobrir todo o edital."
            else:
                next_step = f"🎯 Prioridade de Estudo: Pratique '{top_rec['subject']}' ({top_rec['success_rate']}%). Faltam cerca de {top_rec['needed_for_90']} acertos para os 90%!"
        else:
            next_step = "💪 Continue respondendo questões para consolidar sua taxa de 90% em todos os temas."

        return {
            "overall_success_rate": round(overall_success_rate, 1),
            "questions_answered": total_answered,
            "questions_correct": total_correct,
            "questions_incorrect": total_answered - total_correct,
            "total_time_seconds": stats.total_time_seconds,
            "streak_days": stats.streak_days,
            "meta_target": 90.0,
            "meta_achieved": meta_achieved_flag,
            "meta_progress": round(min(100, (overall_success_rate / 90.0) * 100), 1) if total_answered > 0 else 0,
            "ranking": ranking,
            "ranking_emoji": ranking_emoji,
            "dominados_count": dominados_count,
            "intermediarios_count": intermediarios_count,
            "criticos_count": criticos_count,
            "nao_iniciados_count": nao_iniciados_count,
            "subjects": subjects_detail,
            "study_recommendations": study_recommendations,
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
        
        # Garante ID da questão sempre válido
        raw_id = question.get("id") or ""
        if not raw_id or not str(raw_id).strip():
            content_str = json.dumps(question, sort_keys=True, ensure_ascii=False)
            raw_id = "q_auto_" + hashlib.md5(content_str.encode()).hexdigest()[:32]
            logger.warning(f"Questão sem id válido, gerado hash-based: {raw_id}")
        question_id = str(raw_id).strip()[:100]
        
        # ID composto garante unicidade por (questão, sessão): múltiplos usuários podem responder a mesma questão
        history_id = f"{question_id}_{session_id[:20]}"[:120]
        
        # 1. Registrar histórico
        q_history = QuestionHistory(
            id=history_id,
            question_id=question_id,
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
            error_id = hashlib.md5(f"{question_id}_{session_id}_{datetime.now(timezone.utc).replace(tzinfo=None).timestamp()}".encode()).hexdigest()[:40]
            error_log = ErrorLog(
                id=error_id,
                session_id=session_id,
                subject=subject,
                question_json=json.dumps(question, ensure_ascii=False),
                resolved=False
            )
            db.add(error_log)

            # Gera instantaneamente um Flashcard personalizado para o aluno treinar esta questão errada
            try:
                from flashcards.manager import FlashcardManager
                FlashcardManager.create_card_from_error(db, question, session_id)
            except Exception as e:
                logger.warning(f"Erro ao gerar flashcard automático de erro: {e}")
            
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
            f"📍 **Conceito:** {subject} é tema chave no Questionário de Contratos.\n"
            f"📌 **Artigo-chave:** {article}\n"
            f"⚡ **Pegadinha comum:** {legal_basis[:100]}..."
        )
        
        # Resumo 2min (mais completo)
        summary_2min = (
            f"**Resumo de 2 minutos: {subject}**\n\n"
            f"**O que é?**\n"
            f"No Direito dos Contratos do Código Civil, {subject.lower()} cuida dos pressupostos, "
            f"efeitos e consequências aplicáveis à relação contratual.\n\n"
            f"**Base legal:** {article}\n"
            f"\"{legal_basis[:200]}...\"\n\n"
            f"**Como cai em prova?**\n"
            f"As bancas (OAB, FGV, CESPE, VUNESP) e provas acadêmicas exploram este tema em casos práticos "
            f"com pegadinhas sobre prazos, requisitos essenciais, distinções conceituais e efeitos da má-fé.\n\n"
            f"**Dica do professor:** Revise os requisitos na Escada Ponteana e os prazos decadenciais do Código Civil."
        )
        
        # Resumo 5min (completo, com jurisprudencia e doutrina)
        summary_5min = (
            f"**Resumo de 5 minutos: {subject}**\n\n"
            f"**1. CONCEITO DOUTRINÁRIO**\n"
            f"{subject} compõe o cerne da Teoria Geral dos Contratos e Negócios Jurídicos. "
            f"A doutrina civilista clássica e contemporânea destaca a relevância da boa-fé objetiva (art. 422), "
            f"da função social (art. 421) e dos elementos de existência e validade.\n\n"
            f"**2. FUNDAMENTAÇÃO LEGAL**\n"
            f"Artigo principal: {article}\n"
            f"Texto integral: \"{legal_basis}\"\n\n"
            f"**3. JURISPRUDÊNCIA APLICÁVEL**\n"
            f"O STJ consolidou entendimento sobre a tutela da confiança, a vedação de venire contra factum proprium "
            f"e a preservação da autonomia privada com intervenção mínima.\n\n"
            f"**4. ANÁLISE DO CASO CONCRETO**\n"
            f"{explanation[:300]}...\n\n"
            f"**5. PONTOS DE PROVA (MAIS COBRADOS)**\n"
            f"• Planos da Escada Ponteana (existência, validade e eficácia)\n"
            f"• Distinção entre Emptio Spei e Emptio Rei Speratae\n"
            f"• Ações edilícias (redibitória e estimatória)\n"
            f"• Consequências da ciência prévia do vício (art. 443)\n"
            f"• Aliud pro alio vs. Vício redibitório"
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
