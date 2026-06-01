import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "healthy"


def test_metrics(client):
    r = client.get("/metrics")
    assert r.status_code == 200
    assert b"http_requests_total" in r.data


def test_list_users(client):
    r = client.get("/api/v1/users")
    assert r.status_code == 200
    data = r.get_json()
    assert "users" in data
    assert data["count"] >= 1


def test_get_user(client):
    r = client.get("/api/v1/users/1")
    assert r.status_code == 200
    assert r.get_json()["id"] == 1


def test_get_user_not_found(client):
    r = client.get("/api/v1/users/9999")
    assert r.status_code == 404


def test_create_user(client):
    r = client.post(
        "/api/v1/users",
        json={"name": "Charlie", "email": "charlie@example.com"},
    )
    assert r.status_code == 201
    assert r.get_json()["name"] == "Charlie"
