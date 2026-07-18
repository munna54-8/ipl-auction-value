import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CRICAPI_KEY")

with open("data/raw/player_ids.json", "r", encoding="utf-8") as f:
    player_ids = json.load(f)

test_name = "Virat Kohli"
test_id = player_ids[test_name]

url = "https://api.cricapi.com/v1/players_info"
params = {"apikey": API_KEY, "id": test_id}
response = requests.get(url, params=params, timeout=15)
data = response.json()

print("Status:", data.get("status"))
print(json.dumps(data, indent=2)[:2000])