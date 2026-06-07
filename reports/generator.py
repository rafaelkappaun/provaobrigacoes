from sqlalchemy.orm import Session
from database.models import TopicMastery, UserStats, QuestionHistory
from ai.manager import AIProviderManager
from typing import Dict, Any, List

class ReportGenerator:
    @classmethod
    def generate_cognitive_report(cls, db: Session, session_id: str = "default") -> Dict[str, Any]:
        """Gera um relatório cognitivo com recomendações geradas por IA ou fallback estruturado"""
        topics = db.query(TopicMastery).filter(TopicMastery.session_id == session_id).all()
        stats = db.query(UserStats).filter(UserStats.session_id == session_id).first()
        
        # Filtra tópicos por nível de proficiência
        criticos = [t.subject for t in topics if t.status == "Critico"]
        intermediarios = [t.subject for t in topics if t.status == "Intermediario"]
        dominados = [t.subject for t in topics if t.status == "Dominado"]
        
        # Encontra os 3 piores temas com pelo menos 1 resposta
        worst_topics = sorted(
            [t for t in topics if t.questions_answered > 0], 
            key=lambda x: x.success_rate
        )[:3]
        
        # Constrói o diagnóstico de recomendação
        worst_names = [t.subject for t in worst_topics]
        
        if not worst_names:
            # Se não respondeu nada ainda
            worst_names = ["Mora do devedor", "Dação em pagamento", "Novação"]
            recommendation_txt = (
                "Você ainda não iniciou suas sessões de estudo. "
                "Recomendamos responder a pelo menos 15 questões de Mora, Dação em Pagamento e Novação para calibrar o sistema adaptativo."
            )
        else:
            joined_names = ", ".join(worst_names)
            recommendation_txt = (
                f"Você apresenta dificuldades em {joined_names}. "
                f"Recomendação: responder mais 15 questões destes temas específicos."
            )

        # Prompt para a IA gerar um parecer pedagógico customizado
        prompt = (
            f"Você é um Professor Particular de Direito Civil especialista em concursos públicos.\n"
            f"Analise o seguinte perfil de desempenho do aluno em Direito das Obrigações:\n\n"
            f"- Taxa global de acertos: {round((stats.questions_correct / stats.questions_answered * 100) if stats and stats.questions_answered > 0 else 0.0, 1)}%\n"
            f"- Temas Críticos: {', '.join(criticos) if criticos else 'Nenhum'}\n"
            f"- Temas Intermediários: {', '.join(intermediarios) if intermediarios else 'Nenhum'}\n"
            f"- Temas Dominados: {', '.join(dominados) if dominados else 'Nenhum'}\n"
            f"- Temas com pior taxa de acerto: {', '.join([f'{t.subject} ({round(t.success_rate, 1)}%)' for t in worst_topics])}\n\n"
            f"Gere um parecer curto (máximo 3 parágrafos) analisando a situação cognitiva do estudante, indicando as pegadinhas que ele provavelmente está caindo nesses temas fracos e traçando um roteiro estratégico de estudos para alcançar 95% de acertos."
        )

        # Tenta IA se configurada
        ai_diagnostic = None
        config = AIProviderManager.get_config()
        active_prov = config.get("active_provider", "offline")
        
        if active_prov != "offline":
            for current_prov in [active_prov, "gemini", "openrouter"]:
                key = config.get(f"{current_prov}_api_key")
                if not key:
                    continue
                try:
                    ai_diagnostic = AIProviderManager._call_text_provider(current_prov, key, prompt, 0.6)
                    if ai_diagnostic:
                        break
                except Exception:
                    pass

        # Se falhar ou estiver offline, monta o parecer de fallback estruturado
        if not ai_diagnostic:
            ai_diagnostic = cls._generate_offline_diagnostic(criticos, intermediarios, worst_names)

        return {
            "overall_accuracy": round((stats.questions_correct / stats.questions_answered * 100) if stats and stats.questions_answered > 0 else 0.0, 1),
            "questions_answered": stats.questions_answered if stats else 0,
            "critical_count": len(criticos),
            "intermediate_count": len(intermediarios),
            "mastered_count": len(dominados),
            "recommendation": recommendation_txt,
            "diagnostic": ai_diagnostic,
            "weakest_topics": worst_names
        }

    @staticmethod
    def _generate_offline_diagnostic(criticos: List[str], intermediarios: List[str], worst_names: List[str]) -> str:
        """Gera o parecer textual estruturado de forma dinâmica quando offline"""
        if not criticos and not intermediarios:
            return (
                "Análise Geral: Seu perfil de estudos está em fase inicial de calibração. Para formularmos um diagnóstico "
                "cognitivo detalhado, continue respondendo às questões propostas. O foco inicial deve ser a compreensão geral "
                "dos institutos de Adimplemento (arts. 304 a 388 do CC) e Inadimplemento (arts. 389 a 420 do CC)."
            )
            
        weak_joined = ", ".join(worst_names)
        
        diagnostic = (
            f"Análise Geral: Com base nas suas respostas, observamos um gargalo de aprendizado concentrado em: {weak_joined}. "
            f"Geralmente, erros nestes temas decorrem da confusão entre institutos semelhantes. Por exemplo, na Novação (art. 360), "
            f"a obrigação anterior é extinta com a criação de uma nova, enquanto na Sub-rogação (art. 346) há mera substituição do credor "
            f"com a manutenção das garantias originais. Em Mora (art. 394), as bancas costumam explorar as diferenças práticas entre "
            f"a culpa do devedor e a recusa injustificada do credor (art. 400).\n\n"
            f"Roteiro de Estudos Sugerido:\n"
            f"1. Reler com atenção os artigos do Código Civil referentes a estes temas críticos.\n"
            f"2. Utilizar a biblioteca de artigos do painel para revisar as dicas de prova e pegadinhas comuns.\n"
            f"3. Responder a pelo menos 10 flashcards diários dos assuntos afetados para fortalecer a memória de longo prazo.\n"
            f"4. Acionar o botão 'Treinar Apenas Meus Erros' para refazer as questões incorretas."
        )
        return diagnostic
