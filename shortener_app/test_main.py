from starlette.testclient import TestClient
from .main import app

client = TestClient(app)

def test_register_url():
    response = client.post(
        "/urls/register",
        json={"url": "https://fastapi.tiangolo.com/tutorial/testing/"}
    )
    assert response.status_code == 200

def test_register_url_failed():
    response = client.post(
        "/urls/register",
        json={"url": "hamish_test"}
    )
    assert response.status_code == 422

def test_redirect_url():
    client.post(
        "/urls/register",
        json={"url": "https://github.com/hamishtomato/url_shortener/blob/develop/shortener_app/database.py"}
    )
    response = client.get("/c054116b76", allow_redirects=False)
    assert response.status_code == 307

def test_redirect_url_failed():
    response = client.get("/@123", allow_redirects=False)
    assert response.status_code == 404