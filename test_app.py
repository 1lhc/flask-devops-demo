from app import app, quotes

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.data.decode()
    assert data in quotes or "<h1>" in data

def test_health():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b"OK"
