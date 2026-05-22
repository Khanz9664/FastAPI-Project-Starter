from fastapi.testclient import TestClient
from app.main import app
from app.api.v1.auth import create_access_token

client = TestClient(app)

def test_read_main():
    response = client.get("/api/v1/")
    assert response.status_code == 200
    assert response.json() == {"success": True, "message": "Hello World"}

def test_create_user():
    user_data = {
        "email": "test111@example.com",
        "password": "secret",
        "full_name": "Test User"
    }
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["success"] is True
    assert "data" in response_data
    assert "email" in response_data["data"]

def test_rate_limiting():
    # Send 11 requests, 11th should be rate limited (10/minute)
    for _ in range(10):
        client.get("/api/v1/")
    
    response = client.get("/api/v1/")
    assert response.status_code == 429
    data = response.json()
    assert data["success"] is False
    assert data["message"] == "Too many requests"
    assert data["error_code"] == "RATE_LIMIT_EXCEEDED"

def test_rbac_missing_token():
    response = client.get("/api/v1/users/admin")
    assert response.status_code == 401

def test_rbac_admin_user_roles():
    from app.api.deps.security import get_current_user
    from app.models.base import User
    from app.schemas.users import UserRole
    
    # Override get_current_user to return a dummy normal user
    dummy_user = User(email="test111@example.com", role=UserRole.USER)
    app.dependency_overrides[get_current_user] = lambda: dummy_user
    
    # Try to hit admin endpoint
    admin_resp = client.get("/api/v1/users/admin")
    assert admin_resp.status_code == 403
    
    # Clean up override
    app.dependency_overrides.clear()

