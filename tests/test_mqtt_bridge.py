from backend.common.schemas import Telemetry

sample = {
    "device_id": "d1",
    "timestamp": "2023-01-01T00:00:00Z",
    "voltage": 310.0,
    "current": 25.0,
    "temperature": 30.0,
    "soc": 88.0,
}

def test_telemetry_schema():
    t = Telemetry(**sample)
    assert t.device_id == "d1"
