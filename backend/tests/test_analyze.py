import os
os.environ["DATABASE_PATH"] = ":memory:"

from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_empty_message_rejected():
    response = client.post("/api/analyze-message", json={"message": "   "})
    assert response.status_code in (400, 422)

def test_analyze_returns_expected_fields():
    response = client.post(
        "/api/analyze-message",
        json={"message": "Urgent! Pay immediately using UPI or your account will be blocked."}
    )
    assert response.status_code == 200
    body = response.json()
    assert 1 <= body["threat_score"] <= 100
    assert "threat_category" in body
    assert "safe_next_steps" in body
