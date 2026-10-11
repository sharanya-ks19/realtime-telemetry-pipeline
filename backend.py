import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List
import datetime

app = FastAPI()

class TelemetryData(BaseModel):
    device_id: str
    speed: float
    temperature: float
    timestamp: str = None

# Cache to store recent telemetry entries
latest_data_cache = []

@app.post("/ingest")
async def ingest_data(data: TelemetryData):
    if not data.timestamp:
        data.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    payload = data.dict()
    latest_data_cache.append(payload)
    
    # Keep only the last 50 items in memory
    if len(latest_data_cache) > 50:
        latest_data_cache.pop(0)

    return {"status": "success", "received": payload}

# --- NEW GET ENDPOINT ---
@app.get("/latest")
async def get_latest():
    return latest_data_cache