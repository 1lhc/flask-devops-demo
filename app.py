"""flask-devops-demo application.

This module defines the Flask application for the demo service. It provides:
- `/`        : renders a random motivational quote into `index.html`
- `/health`  : simple JSON health check for container orchestration
- `/metrics` : basic JSON metrics (e.g., quote count)

The app is intended to run under a production WSGI server (Gunicorn).
The development server block is intentionally commented out.
"""

from flask import Flask, render_template, jsonify
import random
import logging
from datetime import datetime, timezone

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

quotes = [
    "Manifesting big moves, one day at a time.",
    "Push yourself; nobody else is going to do it for you.",
    "Less perfection, more authenticity.",
    "Dream big. Act now.",
    "Hustle quietly, let the algorithm do the noise.",
    "Small steps daily = big glow-up.",
    "Dream big, work hard, and make it happen.",
    "Small steps every day lead to big changes.",
    "Hustle until your haters ask if you're hiring.",
    "Stay focused, stay hungry, stay humble.",
    "Every day is a fresh start; make it count.",
    "Believe in yourself, and you're halfway there!",
    "The glow-up is real; it just takes time.",
    "Not every day is a cheat day; keep it balanced.",
    "Discipline isn't daily perfection. It's consistent intention.",
    "Consistency > perfection. Keep going anyway.",
]


@app.route("/")
def home():
    quote = random.choice(quotes)
    logger.info(f"Quote served: {quote}")
    return render_template("index.html", quote=quote)


@app.route("/health")
def health():
    """Health check endpoint for monitoring"""
    return (
        jsonify(
            {
                "status": "healthy",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "service": "flask-devops-demo",
            }
        ),
        200,
    )


@app.route("/metrics")
def metrics():
    """Basic metrics endpoint for monitoring"""
    return (
        jsonify(
            {
                "quote_count": len(quotes),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        ),
        200,
    )


# comment out development server block (not for production)
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)
