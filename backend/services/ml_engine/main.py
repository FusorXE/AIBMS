from fastapi import FastAPI
from typing import Dict
from backend.common.schemas import PredictionResponse
from datetime import datetime
import random

app = FastAPI(title="ML Engine")

@app.get("/predict/{device_id}", response_model=PredictionResponse)
def predict(device_id: str):
    # Dummy model — replace with real inference
    soh = round(random.uniform(80, 100), 2)
    action = "charge" if soh < 90 else "standby"
    return PredictionResponse(
        device_id=device_id,
        timestamp=datetime.utcnow(),
        soh=soh,
        suggested_action=action,
    )
