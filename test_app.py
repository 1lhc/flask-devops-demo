"""Unit tests for the `flask-devops-demo` application.

These tests exercise the main page rendering and the health/metrics
JSON endpoints to ensure they return expected status codes and fields.
"""

from app import app, quotes


def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = response.data.decode()
    # Check if any quote is in the response HTML
    assert any(quote in data for quote in quotes)


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["service"] == "flask-devops-demo"


def test_metrics():
    client = app.test_client()
    response = client.get("/metrics")
    assert response.status_code == 200
    data = response.get_json()
    assert data["quote_count"] == len(quotes)
    assert "timestamp" in data
