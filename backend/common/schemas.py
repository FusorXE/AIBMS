from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Telemetry(BaseModel):
    device_id: str
    timestamp: datetime
    voltage: float
    current: float
    temperature: float
    soc: float

class PredictionResponse(BaseModel):
    device_id: str
    timestamp: datetime
    soh: float
    suggested_action: Optional[str] = None
