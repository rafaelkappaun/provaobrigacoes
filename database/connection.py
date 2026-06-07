import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

logger = logging.getLogger("database")

# Configuração da URL do banco de dados (SQLite por padrão, PostgreSQL em produção/Render)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database/jus_obrigacoes.db")

# Se for SQLite, criamos o diretório 'database' se não existir
if DATABASE_URL.startswith("sqlite:///"):
    db_dir = "database"
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

# Parâmetros adicionais para SQLite para evitar concorrência em requisições concorrentes
connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def run_migrations():
    """Adiciona colunas de session_id se não existirem (migração para multi-usuário)"""
    tables_columns = {
        "user_stats": "session_id",
        "topic_mastery": "session_id",
        "question_history": "session_id",
        "flashcards": "session_id",
        "error_logs": "session_id",
    }
    for table, column in tables_columns.items():
        try:
            with engine.connect() as conn:
                conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} VARCHAR(50) DEFAULT 'default'"))
                conn.commit()
                logger.info(f"Migração: coluna {column} adicionada em {table}")
        except Exception:
            pass
    # Migração: consecutive_correct no topic_mastery
    try:
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE topic_mastery ADD COLUMN consecutive_correct INTEGER DEFAULT 0"))
            conn.commit()
            logger.info("Migração: coluna consecutive_correct adicionada em topic_mastery")
    except Exception:
        pass
    # Migração: groq_api_key no system_config
    try:
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE system_config ADD COLUMN groq_api_key VARCHAR(255) DEFAULT ''"))
            conn.commit()
            logger.info("Migração: coluna groq_api_key adicionada em system_config")
    except Exception:
        pass
    # Migração: mastered no flashcards
    try:
        with engine.connect() as conn:
            conn.execute(text("ALTER TABLE flashcards ADD COLUMN mastered BOOLEAN DEFAULT 0"))
            conn.commit()
            logger.info("Migração: coluna mastered adicionada em flashcards")
    except Exception:
        pass

# Dependência do DB para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
