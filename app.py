from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "FLASH IPTV BACKEND ONLINE"}

@app.post("/login")
def login(data: dict):
    url = data.get("url")
    user = data.get("user")
    pwd = data.get("pass")
    try:
        api = f"{url}/player_api.php?username={user}&password={pwd}"
        r = requests.get(api, timeout=10)
        return r.json()
    except Exception as e:
        return {"error": str(e)}
