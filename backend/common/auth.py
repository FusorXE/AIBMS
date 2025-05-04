import os, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET = os.getenv("JWT_SECRET", "secret")
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET, algorithms=["HS256"])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")


from datetime import datetime, timedelta

def create_token(sub: str, ttl_minutes: int = 60):
    payload = {
        "sub": sub,
        "exp": datetime.utcnow() + timedelta(minutes=ttl_minutes),
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")
