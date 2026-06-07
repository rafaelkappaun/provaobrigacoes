import sys
import os
import tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__))))

import database.connection as db_conn

# Usa um arquivo temporário para testes
TEST_DB_FD, TEST_DB_PATH = tempfile.mkstemp(suffix=".test.db")
os.close(TEST_DB_FD)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.connection import Base

TEST_DB_URL = f"sqlite:///{TEST_DB_PATH}"
engine_test = create_engine(TEST_DB_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)

db_conn.DATABASE_URL = TEST_DB_URL
db_conn.engine = engine_test
db_conn.SessionLocal = TestingSessionLocal

Base.metadata.create_all(bind=engine_test)

from backend.main import app
from backend.session import get_session_id
from database.connection import get_db
from fastapi.testclient import TestClient

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_session_id] = lambda: TEST_SESSION_ID

client = TestClient(app)


TEST_SESSION_ID = "test-session-0000"

def seed_test_data():
    from database.models import UserStats, TopicMastery
    db = TestingSessionLocal()
    if not db.query(UserStats).filter(UserStats.session_id == TEST_SESSION_ID).first():
        db.add(UserStats(session_id=TEST_SESSION_ID, total_time_seconds=3600, questions_answered=50, questions_correct=30, streak_days=5))
        for t in [
            TopicMastery(session_id=TEST_SESSION_ID, subject="Pagamento", success_rate=75.0, status="Intermediario"),
            TopicMastery(session_id=TEST_SESSION_ID, subject="Sub-Rogacao", success_rate=40.0, status="Critico"),
            TopicMastery(session_id=TEST_SESSION_ID, subject="Dacao em Pagamento", success_rate=90.0, status="Dominado"),
        ]:
            db.add(t)
        db.commit()
    db.close()


def setup_module(module):
    seed_test_data()


def teardown_module(module):
    import os
    try:
        os.unlink(TEST_DB_PATH)
    except OSError:
        pass


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "jus-obrigacoes-master"


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_dashboard():
    response = client.get("/api/dashboard")
    assert response.status_code == 200
    data = response.json()
    assert "criticos_count" in data or "success_rate" in data
    assert data.get("questions_answered", 0) > 0 or data.get("total_questions", 0) > 0


def test_articles():
    response = client.get("/api/articles")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_articles_query():
    response = client.get("/api/articles?query=304")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_flashcards():
    response = client.get("/api/flashcards")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_errors():
    response = client.get("/api/errors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_config_masks_api_keys():
    response = client.get("/api/config")
    assert response.status_code == 200
    data = response.json()
    for key in data:
        if key.endswith("_api_key") and data[key]:
            val = str(data[key])
            assert "***" in val or len(val) < 12, f"Key {key} not masked: {val}"


def test_analytics():
    response = client.get("/api/analytics")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_cognitive_report():
    response = client.get("/api/report")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_rate_limit_returns_429():
    for _ in range(35):
        client.get("/api/config")
    response = client.get("/api/config")
    assert response.status_code == 429
