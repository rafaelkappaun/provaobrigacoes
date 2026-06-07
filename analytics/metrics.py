from datetime import datetime, timedelta
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from sqlalchemy import func, Integer, case
from database.models import TopicMastery, UserStats, QuestionHistory

# Grupos de assuntos
ADIMPLEMENTO_TOPICS = [
    "Pagamento - Geral",
    "Quem deve pagar",
    "A quem se deve pagar",
    "Objeto do pagamento e sua prova",
    "Lugar do pagamento",
    "Tempo do pagamento",
    "Consignação em pagamento",
    "Pagamento com sub-rogação",
    "Imputação do pagamento",
    "Dação em pagamento",
    "Novação",
    "Compensação",
    "Confusão",
    "Remissão das dívidas"
]

INADIMPLEMENTO_TOPICS = [
    "Inadimplemento - Disposições gerais",
    "Mora - Geral",
    "Mora do devedor",
    "Mora do credor",
    "Inadimplemento absoluto",
    "Perdas e danos",
    "Juros legais",
    "Cláusula penal",
    "Arras ou sinal"
]

class AnalyticsMetrics:
    @staticmethod
    def get_advanced_analytics(db: Session, session_id: str = "default") -> Dict[str, Any]:
        """Calcula métricas detalhadas de desempenho e histórico de estudos"""
        topics = db.query(TopicMastery).filter(TopicMastery.session_id == session_id).all()
        stats = db.query(UserStats).filter(UserStats.session_id == session_id).first()
        
        # 1. Agrupamento por Categoria (Adimplemento vs Inadimplemento)
        adimp_total = 0
        adimp_correct = 0
        inad_total = 0
        inad_correct = 0
        
        for t in topics:
            if t.subject in ADIMPLEMENTO_TOPICS:
                adimp_total += t.questions_answered
                adimp_correct += t.questions_correct
            elif t.subject in INADIMPLEMENTO_TOPICS:
                inad_total += t.questions_answered
                inad_correct += t.questions_correct
                
        adimp_rate = (adimp_correct / adimp_total * 100.0) if adimp_total > 0 else 0.0
        inad_rate = (inad_correct / inad_total * 100.0) if inad_total > 0 else 0.0
        
        # 2. Desempenho por Banca
        bank_stats = db.query(
            QuestionHistory.bank,
            func.count(QuestionHistory.id).label("total"),
            func.sum(case((QuestionHistory.is_correct == True, 1), else_=0)).label("correct")
        ).filter(QuestionHistory.session_id == session_id).group_by(QuestionHistory.bank).all()
        
        by_bank = []
        for row in bank_stats:
            total = row.total or 0
            correct = row.correct or 0
            rate = (correct / total * 100.0) if total > 0 else 0.0
            by_bank.append({
                "bank": row.bank,
                "total": total,
                "correct": correct,
                "rate": round(rate, 1)
            })
            
        # 3. Histórico dos últimos 7 dias (Questões respondidas por dia)
        today = datetime.utcnow().date()
        daily_history = []
        for i in range(6, -1, -1):
            date = today - timedelta(days=i)
            start_dt = datetime.combine(date, datetime.min.time())
            end_dt = datetime.combine(date, datetime.max.time())
            
            day_stats = db.query(
                func.count(QuestionHistory.id).label("total"),
                func.sum(case((QuestionHistory.is_correct == True, 1), else_=0)).label("correct")
            ).filter(
                QuestionHistory.answered_at >= start_dt,
                QuestionHistory.answered_at <= end_dt,
                QuestionHistory.session_id == session_id
            ).first()
            
            daily_history.append({
                "date": date.strftime("%d/%m"),
                "answered": day_stats.total or 0,
                "correct": day_stats.correct or 0
            })
            
        # 4. Totalizadores Gerais
        total_answered = stats.questions_answered if stats else 0
        total_correct = stats.questions_correct if stats else 0
        overall_rate = (total_correct / total_answered * 100.0) if total_answered > 0 else 0.0
        
        return {
            "overall_rate": round(overall_rate, 1),
            "total_answered": total_answered,
            "total_correct": total_correct,
            "categories": [
                {
                    "name": "Adimplemento das Obrigações",
                    "total": adimp_total,
                    "correct": adimp_correct,
                    "rate": round(adimp_rate, 1)
                },
                {
                    "name": "Inadimplemento das Obrigações",
                    "total": inad_total,
                    "correct": inad_correct,
                    "rate": round(inad_rate, 1)
                }
            ],
            "by_bank": by_bank,
            "daily_history": daily_history
        }
