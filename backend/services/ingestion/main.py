from fastapi import FastAPI, Depends
from influxdb_client import InfluxDBClient, Point, WriteApi
import os
from backend.common.schemas import Telemetry
from backend.common.auth import verify_token

bucket = "bms"
org = "fusorx"
url = os.getenv("INFLUX_URL", "http://localhost:8086")
token = os.getenv("INFLUX_TOKEN", "local-dev-token")

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=WriteApi.SYNCHRONOUS)

app = FastAPI(title="Ingestion Service")

@app.post("/ingest", dependencies=[Depends(verify_token)])
def ingest(data: Telemetry):
    point = (Point("telemetry")
             .tag("device_id", data.device_id)
             .field("voltage", data.voltage)
             .field("current", data.current)
             .field("temperature", data.temperature)
             .field("soc", data.soc)
             .time(data.timestamp))
    write_api.write(bucket=bucket, record=point)
    return {"status": "ok"}
