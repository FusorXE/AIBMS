from fastapi import FastAPI
from backend.common.schemas import Telemetry, PredictionResponse
from datetime import datetime
import random

app = FastAPI(title="Scheduler Service")

@app.post("/optimize")
def optimize(data: Telemetry):
    # Placeholder rule‑based optimizer
    if data.soc < 30:
        action = "charge_now"
    elif data.soc > 90 and data.temperature < 30:
        action = "discharge_peak"
    else:
        action = "standby"
    return {
        "device_id": data.device_id,
        "timestamp": datetime.utcnow(),
        "recommended_action": action,
    }
