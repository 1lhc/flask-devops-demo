from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Manifesting big moves, one day at a time.",
    "Push yourself; nobody else is going to do it for you.",
    "Less perfection, more authenticity.",
    "Dream big. Act now.",
    "Hustle quietly, let the algorithm do the noise.",
    "Small steps daily = big glow‑up.",
    "Dream big, work hard, and make it happen.",
    "Small steps every day lead to big changes.",
    "Hustle until your haters ask if you're hiring.",
    "Stay focused, stay hungry, stay humble.",
    "Every day is a fresh start; make it count.",
    "Believe in yourself, and you’re halfway there!",
    "The glow‑up is real; it just takes time.",
    "Not every day is a cheat day; keep it balanced.",
    "Discipline isn’t daily perfection. It’s consistent intention.",
    "Consistency > perfection. Keep going anyway."
]

@app.route("/")
def home():
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
