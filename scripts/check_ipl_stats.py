import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CRICAPI_KEY")

with open("data/raw/player_ids.json", "r", encoding="utf-8") as f:
    player_ids = json.load(f)

test_id = player_ids["Virat Kohli"]
url = "https://api.cricapi.com/v1/players_info"
params = {"apikey": API_KEY, "id": test_id}
response = requests.get(url, params=params, timeout=15)
data = response.json()

ipl_stats = [s for s in data["data"]["stats"] if s["matchtype"] == "ipl"]
print(f"IPL-specific stat entries found: {len(ipl_stats)}")
for s in ipl_stats:
    print(s)