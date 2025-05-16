from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_user():
    user_data = {
        "email": "test@example.com",
        "password": "secret",
        "full_name": "Test User"
    }
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 200
    assert "email" in response.json()
