from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_student_ask():
    response = client.post("/student/ask", json={
        "question": "What is gravity?",
        "grade_level": 8
    })
    assert response.status_code == 200
    assert "Let's break it down" in response.json()["response"]
