import os
import logging
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

logger = logging.getLogger("database")

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database/jus_obrigacoes.db")

if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

is_sqlite = DATABASE_URL.startswith("sqlite:///")
is_postgres = DATABASE_URL.startswith("postgresql://")

if is_sqlite:
    db_dir = "database"
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

connect_args = {}
if is_sqlite:
    connect_args["check_same_thread"] = False
elif is_postgres:
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


ALLOWED_TABLES = {"user_stats", "topic_mastery", "question_history", "flashcards", "error_logs", "system_config"}
ALLOWED_COLUMNS = {
    "session_id", "consecutive_correct", "groq_api_key", "mastered", "last_reviewed",
    "question_id",
}

def _safe_ident(name: str, allowed: set[str]) -> str:
    if name not in allowed:
        raise ValueError(f"Identificador não permitido: {name}")
    return name


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
                safe_table = _safe_ident(table, ALLOWED_TABLES)
                safe_col = _safe_ident(column, ALLOWED_COLUMNS)
                if not column_exists(conn, safe_table, safe_col):
                    conn.execute(text(f"ALTER TABLE {safe_table} ADD COLUMN {safe_col} VARCHAR(50) DEFAULT 'default'"))
                    conn.commit()
                    logger.info(f"Migração: coluna {column} adicionada em {table}")
            except (ValueError, Exception) as e:
                if not isinstance(e, ValueError):
                    logger.debug(f"Migração {table}.{column}: {e}")

        for col_name in ["consecutive_correct", "groq_api_key"]:
            try:
                safe_col = _safe_ident(col_name, ALLOWED_COLUMNS)
                table_name = "topic_mastery" if col_name == "consecutive_correct" else "system_config"
                safe_table = _safe_ident(table_name, ALLOWED_TABLES)
                if not column_exists(conn, safe_table, safe_col):
                    col_def = "INTEGER DEFAULT 0" if col_name == "consecutive_correct" else "VARCHAR(255) DEFAULT ''"
                    conn.execute(text(f"ALTER TABLE {safe_table} ADD COLUMN {safe_col} {col_def}"))
                    conn.commit()
                    logger.info(f"Migração: coluna {col_name} adicionada em {table_name}")
            except (ValueError, Exception) as e:
                if not isinstance(e, ValueError):
                    logger.debug(f"Migração {table_name}.{col_name}: {e}")

        try:
            safe_table = _safe_ident("flashcards", ALLOWED_TABLES)
            safe_col = _safe_ident("mastered", ALLOWED_COLUMNS)
            if not column_exists(conn, safe_table, safe_col):
                default = "0" if is_sqlite else "FALSE"
                conn.execute(text(f"ALTER TABLE {safe_table} ADD COLUMN {safe_col} BOOLEAN DEFAULT {default}"))
                conn.commit()
                logger.info("Migração: coluna mastered adicionada em flashcards")
        except (ValueError, Exception) as e:
            if not isinstance(e, ValueError):
                logger.debug(f"Migração flashcards.mastered: {e}")

        try:
            safe_table = _safe_ident("flashcards", ALLOWED_TABLES)
            safe_col = _safe_ident("last_reviewed", ALLOWED_COLUMNS)
            if not column_exists(conn, safe_table, safe_col):
                conn.execute(text(f"ALTER TABLE {safe_table} ADD COLUMN {safe_col} DATETIME"))
                conn.commit()
                logger.info("Migração: coluna last_reviewed adicionada em flashcards")
        except (ValueError, Exception) as e:
            if not isinstance(e, ValueError):
                logger.debug(f"Migração last_reviewed: {e}")

        # Aumenta VARCHAR de id para 120 em todas as tabelas relevantes (PostgreSQL)
        if not is_sqlite:
            id_tables = ["flashcards", "question_history", "error_logs"]
            for tbl in id_tables:
                try:
                    safe_tbl = _safe_ident(tbl, ALLOWED_TABLES)
                    size_row = conn.execute(text(
                        "SELECT character_maximum_length FROM information_schema.columns "
                        "WHERE table_name = :tbl AND column_name = 'id'"
                    ).bindparams(tbl=safe_tbl)).fetchone()
                    current_size = size_row[0] if size_row else None
                    if current_size is None or current_size < 120:
                        conn.execute(text(f"ALTER TABLE {safe_tbl} ALTER COLUMN id TYPE VARCHAR(120)"))
                        conn.commit()
                        logger.info(f"Migração: {tbl}.id alterado para VARCHAR(120) (era {current_size})")
                    else:
                        logger.info(f"Migração: {tbl}.id já é VARCHAR({current_size}), sem necessidade de alterar")
                except Exception as e:
                    conn.rollback()
                    logger.warning(f"Migração {tbl}.id type falhou: {type(e).__name__}: {e}")

        # Adiciona coluna question_id em question_history
        try:
            safe_tbl = _safe_ident("question_history", ALLOWED_TABLES)
            safe_col = _safe_ident("question_id", ALLOWED_COLUMNS)
            if not column_exists(conn, safe_tbl, safe_col):
                conn.execute(text(f"ALTER TABLE {safe_tbl} ADD COLUMN {safe_col} VARCHAR(120)"))
                conn.commit()
                logger.info("Migração: coluna question_id adicionada em question_history")
        except Exception as e:
            conn.rollback()
            logger.warning(f"Migração question_history.question_id falhou: {type(e).__name__}: {e}")

        # Remove UNIQUE constraint antiga de topic_mastery.subject
        try:
            if is_sqlite:
                indexes = conn.execute(text(
                    "SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='topic_mastery' AND sql IS NOT NULL AND sql LIKE '%UNIQUE%'"
                )).fetchall()
            else:
                indexes = conn.execute(text(
                    "SELECT indexname FROM pg_indexes WHERE tablename='topic_mastery' AND indexdef LIKE '%UNIQUE%'"
                )).fetchall()
            for idx in indexes:
                idx_name = idx[0]
                if "subject" in idx_name.lower():
                    conn.execute(text(f"DROP INDEX IF EXISTS [{idx_name}]") if is_sqlite else text(f"DROP INDEX IF EXISTS \"{idx_name}\""))
                    conn.commit()
                    logger.info(f"Migração: índice UNIQUE {idx_name} removido de topic_mastery")
            if is_sqlite:
                conn.execute(text(
                    "CREATE INDEX IF NOT EXISTS ix_topic_mastery_subject ON topic_mastery(subject)"
                ))
                conn.commit()
                logger.info("Migração: índice não-único ix_topic_mastery_subject recriado")
        except Exception as e:
            logger.debug(f"Migração unique index: {e}")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
