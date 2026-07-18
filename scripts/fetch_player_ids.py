import os
import json
import time
import requests
from dotenv import load_dotenv
from player_list import PLAYERS

load_dotenv()
API_KEY = os.getenv("CRICAPI_KEY")

player_ids = {}

for name in PLAYERS:
    url = "https://api.cricapi.com/v1/players"
    params = {"apikey": API_KEY, "search": name}
    response = requests.get(url, params=params, timeout=15)
    data = response.json()

    hits_used = data.get("info", {}).get("hitsUsed", "?")
    hits_limit = data.get("info", {}).get("hitsLimit", "?")

    if data.get("data"):
        player_ids[name] = data["data"][0]["id"]
        print(f"{name}: found (hits used: {hits_used}/{hits_limit})")
    else:
        print(f"{name}: NOT FOUND (hits used: {hits_used}/{hits_limit})")

    if isinstance(hits_used, int) and isinstance(hits_limit, int) and hits_used >= hits_limit - 2:
        print("\nApproaching daily hit limit — stopping early to save remaining hits for stats pull.")
        break

    time.sleep(1)

os.makedirs("data/raw", exist_ok=True)
with open("data/raw/player_ids.json", "w", encoding="utf-8") as f:
    json.dump(player_ids, f, indent=2)

print(f"\nTotal player IDs collected: {len(player_ids)}")