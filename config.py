"""Configuration for the flask-devops-demo application.

This module defines a base `Config` class with a secret key and the
default list of motivational `QUOTES`. Two subclasses provide simple
overrides for production and development environments.
"""

import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    QUOTES = [
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


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
