import pytest, requests, os, json, jwt, datetime
from backend.common.auth import create_token

BASE = "http://localhost:8000"

def test_login():
    token = create_token("test@fusorx.io")
    assert jwt.decode(token, os.getenv("JWT_SECRET", "secret"), algorithms=["HS256"])["sub"] == "test@fusorx.io"
