# Flask DevOps Demo

This is a simple Flask application containerized using Docker, meant for practicing DevOps workflows.

## Features

- Simple Flask API that returns "Hello from DevOps demo!"
- Containerized using Docker
- Automatically tested using GitHub Actions (CI)

## Running Locally

Make sure Docker is installed and running.

```bash
docker build -t flask-devops-demo .
docker run -p 5001:5000 flask-devops-demo
```

Visit http://127.0.0.1:5001

## File Structure

```bash
flask-devops-demo/
├── app.py
├── Dockerfile
├── requirements.txt
├── .github/
│ └── workflows/
│ └── python-app.yml
└── README.md
```
