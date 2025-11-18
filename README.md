# Flask DevOps Demo

A simple Flask web application containerized using Docker, with automated testing (CI) using GitHub Actions.

## 🚀 Features

- **Flask Web App:** Returns random motivational quotes and provides a `/health` endpoint.
- **Unit Testing:** Uses `pytest` for automated testing.
- **Docker Containerization:** Packages the app so it runs consistently on any system.
- **CI Integration:** Tests run automatically on every push via GitHub Actions.

## File Structure

```
flask-devops-demo/
├── app.py
├── Dockerfile
├── requirements.txt
├── test_app.py
├── .github/
│   └── workflows/
│       └── python-app.yml
└── README.md
```

## 🛠️ Prerequisites

- Docker Desktop installed on your system
- Python 3.8 or newer
- A GitHub account

## 🧪 Local Setup

```bash
git clone https://github.com/1lhc/flask-devops-demo.git
cd flask-devops-demo

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install runtime deps (and tests when present)
pip install -r requirements.txt

# Run the app locally (development):
# - The repository is configured to run under Gunicorn in production.
# - For quick local testing you can use Flask's dev server (not for prod):
python -m flask run --port 5000
```

Open your browser to http://localhost:5000

## 🧪 Run Tests

Install test tools (if not installed) and run the suite:

```bash
# If you haven't created the venv yet:
python3 -m venv .venv
source .venv/bin/activate

# Install project deps + pytest for testing
pip install -r requirements.txt pytest

# Run tests
pytest -q
```

## 🐳 Docker Containerization

This project is containerized using Docker for consistent deployments. The
container runs the app under Gunicorn and listens on port `8000`.

### Build and Run Locally

```bash
# Build the Docker image
docker build -t flask-devops-demo .

# Run the container (maps container 8000 -> host 8000)
docker run -p 8000:8000 flask-devops-demo
```

Open your browser to http://localhost:8000

### Helpful container tips

```bash
# Get a shell inside a running container
docker exec -it <container_id> /bin/sh

# Inspect container environment
cat /etc/os-release
python --version
pip list
```

## ✅ CI with GitHub Actions

Tests are automatically run on every push or pull request to `main`. Check the **Actions** tab in the GitHub repository for results.

## 🎯 Why This Project Matters

- Shows ability to set up a **CI pipeline**
- Demonstrates proficiency in **Docker containerization**
