import json
import os
import time
import random
import paho.mqtt.publish as publish

BROKER = os.getenv("MQTT_BROKER", "localhost")
TOPIC = os.getenv("MQTT_TOPIC", "telemetry/device1")

while True:
    payload = {
        "device_id": "device1",
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        "voltage": round(random.uniform(300, 350), 2),
        "current": round(random.uniform(20, 40), 2),
        "temperature": round(random.uniform(20, 40), 2),
        "soc": round(random.uniform(50, 100), 2),
    }
    publish.single(TOPIC, json.dumps(payload), hostname=BROKER)
    time.sleep(1)
