from app.main import app

def test_hello():
    client = app.test_client()
    response = client.get("/hello")
    data = response.get_json()
    assert data["message"] == "Hello, World!"


def test_db_connected():
    client = app.test_client()
    response = client.get("/db")
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "connected"
