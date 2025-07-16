def test_index():
    from app import app
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello from DevOps demo!" in response.data
