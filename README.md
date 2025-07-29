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

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py  # Runs the Flask app locally
```

## 🐳 Running with Docker

```bash
docker build -t flask-devops-demo .
docker run -p 5001:5000 flask-devops-demo
```

Open your browser to [http://localhost:5001](http://localhost:5001)

## ✅ CI with GitHub Actions

Tests are automatically run on every push or pull request to `main`. Check the **Actions** tab in the GitHub repository for results.

## 🎯 Why This Project Matters

- Shows ability to set up a **CI pipeline**
- Demonstrates proficiency in **Docker containerization**
