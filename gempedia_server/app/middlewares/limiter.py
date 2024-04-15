# limiter.py
from slowapi import Limiter


def setup_limiter():
    # Rate limiting setup
    limiter = Limiter(key_func=lambda: "global", default_limits=["100 per minute"])
    return limiter
