from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from collections import defaultdict
import time

app = FastAPI()

rate_limit_data = defaultdict(list)

alerts = []

THRESHOLD = 100

class Telemetry(BaseModel):
    device_id: str
    metric: str
    value : float

@app.post("/api/telemetry")
def receive_telemetry(data: Telemetry):
    current_time = time.time()

    timestamps = rate_limit_data[data.device_id]
    timestamps = [t for t in timestamps if current_time - t < 10]
    
    if len(timestamps) >=3:
        raise HTTPException(
            status_code= 404,
            detais = "Too Many Request"
        )
    timestamps.append(current_time)
    rate_limit_data[data.device_id] = timestamps

    if data.metric == "temperature" and data.value > THRESHOLD:
        alert = {
            "id": len(alert) + 1,
            "device_id": data.device_id,
            "metric":data.metric,
            "value":data.value,
            "timestamp": current_time
        }
        alert.append(alert)

        return{
            "message": "Telemetry received"
        }

@app.get("/api/alerts")
def get_alerts():
    return alerts

@app.post("/api/delete/{alert_id}")
def delete_alert(alert_id: int):
    global alerts

    for alert in alerts:
        if alert["id"] == alert_id:
            alerts.remove(alert)
            return{"message": "Alert dismissed"}
    
    raise HTTPException(
        status_code=404,
        detail= "Alert not found"
    )


