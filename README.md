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
Open your browser to [http://localhost:5000](http://localhost:5000)

## 🐳 Docker Containerization

This project is containerized using Docker for consistent deployments.

### Build and Run Locally
```bash
# Build the Docker image
docker build -t flask-devops-demo .

# Run the container
docker run -p 5001:5000 flask-devops-demo

# Use this to check what OS
docker run -it --rm python:3.12-slim cat /etc/os-release

# OR Get a shell inside the container
docker exec -it <container_id> /bin/bash

# Once inside, you can explore:
cat /etc/os-release    # Check the Linux distribution
python --version       # Check Python version
pip list               # See installed packages
```
Open your browser to [http://localhost:5001](http://localhost:5001)

## ✅ CI with GitHub Actions

Tests are automatically run on every push or pull request to `main`. Check the **Actions** tab in the GitHub repository for results.

## 🎯 Why This Project Matters

- Shows ability to set up a **CI pipeline**
- Demonstrates proficiency in **Docker containerization**
