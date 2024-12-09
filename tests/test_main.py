from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_shorten_url():
    response = client.post("/shorten/", json={"original_url": "http://example.com"})
    assert response.status_code == 200
    assert "short_url" in response.json()


def test_redirect_url():
    short_id = "abc123"
    app.database[short_id] = {"original_url": "http://example.com", "short_id": short_id}
    response = client.get(f"/{short_id}")
    assert response.status_code == 200
    assert response.json() == {"original_url": "http://example.com"}
