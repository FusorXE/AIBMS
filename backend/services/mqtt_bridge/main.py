import os
import json
import asyncio
from pydantic import ValidationError
from fastapi import FastAPI
import httpx
import paho.mqtt.client as mqtt
from backend.common.schemas import Telemetry

BROKER_URL = os.getenv("MQTT_BROKER", "mqtt")
BROKER_PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = os.getenv("MQTT_TOPIC", "telemetry/#")
INGEST_URL = os.getenv("INGEST_URL", "http://ingestion:8000/ingest")
JWT_TOKEN = os.getenv("JWT_TOKEN", "")

app = FastAPI(title="MQTT Bridge")

queue: asyncio.Queue = asyncio.Queue()

# MQTT callbacks

def on_connect(client, userdata, flags, rc):
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        queue.put_nowait(payload)
    except Exception:
        pass


async def worker():
    async with httpx.AsyncClient() as session:
        while True:
            data = await queue.get()
            try:
                telem = Telemetry(**data)
            except ValidationError:
                continue
            headers = {}
            if JWT_TOKEN:
                headers["Authorization"] = f"Bearer {JWT_TOKEN}"
            await session.post(INGEST_URL, json=telem.dict(), headers=headers)
            queue.task_done()


@app.on_event("startup")
async def startup_event():
    loop = asyncio.get_event_loop()
    loop.create_task(worker())
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_URL, BROKER_PORT, 60)
    loop.create_task(asyncio.to_thread(client.loop_forever))

