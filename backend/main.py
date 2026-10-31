from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from microservices import sec_to_minute, sendEmail

import psutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:3000', 'http://localhost:3000', 'http://127.0.0.1:5500', 'http://localhost:5500', "https://battery-monitor-0dav.onrender.com/"],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*']
)

class Model(BaseModel):
    pass

class Battery(Model):
    percent: float
    power_plugged: bool
    estimate: int

@app.get('/battery')
def batteryf():
    battery = psutil.sensors_battery()

    if battery is None:
        raise HTTPException(
            status_code=404,
            detail="Informações da bateria indisponíveis"
        )

    minutes_left = sec_to_minute(battery.secsleft)

    return Battery(
        percent=battery.percent,
        power_plugged=battery.power_plugged,
        estimate=minutes_left
    )

@app.post('/send')
def sendMessage(battery: Battery):
    percent = battery.percent
    sendEmail(percent, battery.power_plugged)