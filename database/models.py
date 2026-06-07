from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from database.connection import Base

def _utcnow():
    return datetime.now(timezone.utc).replace(tzinfo=None)

class UserStats(Base):
    __tablename__ = "user_stats"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(50), index=True, default="default")
    total_time_seconds = Column(Integer, default=0)
    questions_answered = Column(Integer, default=0)
    questions_correct = Column(Integer, default=0)
    streak_days = Column(Integer, default=0)
    last_study_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=_utcnow)

class TopicMastery(Base):
    __tablename__ = "topic_mastery"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(50), index=True, default="default")
    subject = Column(String(100), index=True, nullable=False)
    questions_answered = Column(Integer, default=0)
    questions_correct = Column(Integer, default=0)
    consecutive_errors = Column(Integer, default=0)
    success_rate = Column(Float, default=0.0) # de 0.0 a 100.0
    status = Column(String(20), default="Critico") # "Critico", "Intermediario", "Dominado"
    
    # Novo: acertos consecutivos para dominar (precisa de 5)
    consecutive_correct = Column(Integer, default=0)
    
    # Repetição Espaçada (SM-2 para o tema)
    ease_factor = Column(Float, default=2.5)
    interval_days = Column(Integer, default=0)
    next_revision_date = Column(DateTime, nullable=True)

class QuestionHistory(Base):
    __tablename__ = "question_history"
    
    id = Column(String(50), primary_key=True, index=True) # question UUID
    session_id = Column(String(50), index=True, default="default")
    subject = Column(String(100), index=True, nullable=False)
    difficulty = Column(String(20), nullable=False) # "Facil", "Medio", "Dificil"
    bank = Column(String(50), nullable=False) # "FGV", "CESPE", etc.
    is_correct = Column(Boolean, nullable=False)
    response_time = Column(Float, default=0.0) # em segundos
    is_insecure = Column(Boolean, default=False) # Acerto inseguro (tempo > 45s)
    answered_at = Column(DateTime, default=_utcnow)

class Flashcard(Base):
    __tablename__ = "flashcards"
    
    id = Column(String(120), primary_key=True, index=True)
    session_id = Column(String(50), index=True, default="default")
    subject = Column(String(100), index=True, nullable=False)
    front = Column(Text, nullable=False)
    back = Column(Text, nullable=False)
    
    # SM-2 para Flashcard
    ease_factor = Column(Float, default=2.5)
    interval_days = Column(Integer, default=0)
    next_revision_date = Column(DateTime, default=_utcnow)
    last_reviewed = Column(DateTime, nullable=True)
    box = Column(Integer, default=1) # Caixa do Leitner/SM-2
    mastered = Column(Boolean, default=False) # Usuário marcou como dominado
    created_at = Column(DateTime, default=_utcnow)

class ErrorLog(Base):
    __tablename__ = "error_logs"
    
    id = Column(String(50), primary_key=True, index=True)
    session_id = Column(String(50), index=True, default="default")
    subject = Column(String(100), index=True, nullable=False)
    question_json = Column(Text, nullable=False) # JSON da questão errada
    answered_at = Column(DateTime, default=_utcnow)
    resolved = Column(Boolean, default=False)

class SystemConfig(Base):
    __tablename__ = "system_config"
    
    id = Column(Integer, primary_key=True, index=True)
    active_provider = Column(String(50), default="offline") # "offline", "gemini", "openrouter", "deepseek", "qwen", "mistral"
    gemini_api_key = Column(String(255), default="")
    openrouter_api_key = Column(String(255), default="")
    deepseek_api_key = Column(String(255), default="")
    qwen_api_key = Column(String(255), default="")
    mistral_api_key = Column(String(255), default="")
    groq_api_key = Column(String(255), default="")
    temperature = Column(Float, default=0.3)
