from fastapi import FastAPI, HTTPException, Depends
import httpx, os
from backend.common.auth import verify_token
from backend.common.schemas import Telemetry, PredictionResponse

INGEST_URL = os.getenv("INGEST_URL", "http://ingestion:8000/ingest")
PREDICT_URL = os.getenv("PREDICT_URL", "http://ml_engine:8000/predict")

app = FastAPI(title="API Gateway")

fake_users = {"demo@fusorx.io": "demo123"}

@app.post("/login")
def login(credentials: dict):
    email = credentials.get("email")
    password = credentials.get("password")
    if fake_users.get(email) != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(sub=email)
    return {"access_token": token}


@app.post("/telemetry")
async def post_telemetry(data: Telemetry, token=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        r = await client.post(INGEST_URL, json=data.dict(), headers={"Authorization": f"Bearer {token['sub']}"})
        if r.status_code != 200:
            raise HTTPException(status_code=502, detail="Ingestion failed")
    return {"status": "accepted"}

@app.get("/prediction/{device_id}", response_model=PredictionResponse)
async def get_prediction(device_id: str, token=Depends(verify_token)):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{PREDICT_URL}/{device_id}")
        if r.status_code != 200:
            raise HTTPException(status_code=502, detail="ML service error")
        return r.json()
