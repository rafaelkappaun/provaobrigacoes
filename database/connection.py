import os
import logging
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

logger = logging.getLogger("database")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database/jus_obrigacoes.db")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

is_sqlite = DATABASE_URL.startswith("sqlite:///")

if is_sqlite:
    db_dir = "database"
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

connect_args = {}
if is_sqlite:
    connect_args["check_same_thread"] = False
else:
    connect_args["sslmode"] = "require"

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
    pool_recycle=300,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def column_exists(conn, table_name, column_name):
    inspector = inspect(conn)
    columns = [c["name"] for c in inspector.get_columns(table_name)]
    return column_name in columns


def run_migrations():
    tables_columns = {
        "user_stats": "session_id",
        "topic_mastery": "session_id",
        "question_history": "session_id",
        "flashcards": "session_id",
        "error_logs": "session_id",
    }
    with engine.connect() as conn:
        for table, column in tables_columns.items():
            try:
                if not column_exists(conn, table, column):
                    conn.execute(text(f"ALTER TABLE {table} ADD COLUMN {column} VARCHAR(50) DEFAULT 'default'"))
                    conn.commit()
                    logger.info(f"Migração: coluna {column} adicionada em {table}")
            except Exception:
                pass

        for col_name, col_def in [
            ("consecutive_correct", "INTEGER DEFAULT 0"),
            ("groq_api_key", "VARCHAR(255) DEFAULT ''"),
        ]:
            try:
                if not column_exists(conn, "topic_mastery" if col_name == "consecutive_correct" else "system_config", col_name):
                    table_name = "topic_mastery" if col_name == "consecutive_correct" else "system_config"
                    conn.execute(text(f"ALTER TABLE {table_name} ADD COLUMN {col_name} {col_def}"))
                    conn.commit()
                    logger.info(f"Migração: coluna {col_name} adicionada em {table_name}")
            except Exception:
                pass

        try:
            if not column_exists(conn, "flashcards", "mastered"):
                if is_sqlite:
                    conn.execute(text("ALTER TABLE flashcards ADD COLUMN mastered BOOLEAN DEFAULT 0"))
                else:
                    conn.execute(text("ALTER TABLE flashcards ADD COLUMN mastered BOOLEAN DEFAULT FALSE"))
                conn.commit()
                logger.info("Migração: coluna mastered adicionada em flashcards")
        except Exception:
            pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
