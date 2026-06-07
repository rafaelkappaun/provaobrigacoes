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
            TopicMastery(session_id=TEST_SESSION_ID, subject="Pagamento - Geral", success_rate=75.0, status="Intermediario"),
            TopicMastery(session_id=TEST_SESSION_ID, subject="Pagamento com sub-rogação", success_rate=40.0, status="Critico"),
            TopicMastery(session_id=TEST_SESSION_ID, subject="Dação em pagamento", success_rate=90.0, status="Dominado"),
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
    # Root pode retornar HTML (Vite) ou JSON


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
    from backend.main import _rate_limit_store
    for _ in range(65):
        client.get("/api/config")
    response = client.get("/api/config")
    assert response.status_code == 429
    _rate_limit_store.clear()


def test_question_next_returns_valid_question():
    """Verifica se o endpoint de próxima questão retorna uma questão válida"""
    response = client.get("/api/question/next?bank=FGV")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "subject" in data
    assert "enunciado" in data
    assert "options" in data
    assert "gabarito" in data
    assert len(data["options"]) >= 2
    assert data["gabarito"] in data["options"]


def test_question_answer_correct():
    """Submete uma resposta correta e verifica o processamento"""
    # Primeiro obtém uma questão
    q_resp = client.get("/api/question/next?bank=FGV")
    assert q_resp.status_code == 200
    question = q_resp.json()
    
    # Submete a resposta com o gabarito
    answer_resp = client.post("/api/question/answer", json={
        "question": question,
        "selected_option": question["gabarito"],
        "response_time": 10.5
    })
    assert answer_resp.status_code == 200
    data = answer_resp.json()
    assert "is_correct" in data
    assert data["is_correct"] == True
    assert "feedback" in data
    assert "topic_status" in data
    assert "topic_success_rate" in data


def test_question_answer_incorrect():
    """Submete uma resposta errada e verifica o feedback de erro"""
    q_resp = client.get("/api/question/next?bank=CESPE")
    assert q_resp.status_code == 200
    question = q_resp.json()
    
    # Escolhe uma opção diferente do gabarito
    wrong_option = [k for k in question["options"].keys() if k != question["gabarito"]][0]
    
    answer_resp = client.post("/api/question/answer", json={
        "question": question,
        "selected_option": wrong_option,
        "response_time": 5.0
    })
    assert answer_resp.status_code == 200
    data = answer_resp.json()
    assert data["is_correct"] == False
    assert data["reinforcement"] is not None  # Deve gerar reforço automático


def test_question_answer_duplicate_returns_409():
    """Enviar a mesma questão duas vezes deve retornar 409"""
    q_resp = client.get("/api/question/next?bank=FGV")
    assert q_resp.status_code == 200
    question = q_resp.json()
    
    # Primeira submissão
    client.post("/api/question/answer", json={
        "question": question,
        "selected_option": question["gabarito"],
        "response_time": 10.0
    })
    
    # Segunda submissão da mesma questão deve falhar
    dup_resp = client.post("/api/question/answer", json={
        "question": question,
        "selected_option": question["gabarito"],
        "response_time": 5.0
    })
    assert dup_resp.status_code == 409


def test_simulado_start_returns_questions():
    """Verifica se o simulado retorna uma lista de questões"""
    response = client.get("/api/simulado/start?size=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5
    for q in data:
        assert "id" in q
        assert "enunciado" in q
        assert "options" in q
        assert "gabarito" in q


def test_vespera_start_returns_questions():
    """Verifica se o modo véspera retorna 50 questões"""
    response = client.get("/api/vespera/start")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 50
