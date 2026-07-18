import os
import json
import time
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CRICAPI_KEY")

with open("data/raw/player_ids.json", "r", encoding="utf-8") as f:
    player_ids = json.load(f)

def clean_stats(raw_stats):
    """Dedupe stats, stripping whitespace from keys, keeping the LAST occurrence
    (API appears to append updated blocks after older ones)."""
    cleaned = {}
    for s in raw_stats:
        if s["matchtype"] != "ipl":
            continue
        key = (s["fn"], s["stat"].strip())
        try:
            value = float(str(s["value"]).strip())
        except ValueError:
            value = s["value"].strip()
        cleaned[key] = value
    return cleaned

all_players = []

for name, pid in player_ids.items():
    url = "https://api.cricapi.com/v1/players_info"
    params = {"apikey": API_KEY, "id": pid}
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        raw_stats = data.get("data", {}).get("stats", [])
        stats = clean_stats(raw_stats)

        row = {
            "name": name,
            "role": data.get("data", {}).get("role", ""),
            "ipl_matches": stats.get(("batting", "m")),
            "ipl_runs": stats.get(("batting", "runs")),
            "ipl_bat_avg": stats.get(("batting", "avg")),
            "ipl_bat_sr": stats.get(("batting", "sr")),
            "ipl_100s": stats.get(("batting", "100s"), stats.get(("batting", "100"))),
            "ipl_50s": stats.get(("batting", "50s"), stats.get(("batting", "50"))),
            "ipl_wkts": stats.get(("bowling", "wkts")),
            "ipl_bowl_avg": stats.get(("bowling", "avg")),
            "ipl_economy": stats.get(("bowling", "econ")),
        }
        all_players.append(row)
        print(f"{name}: OK (matches={row['ipl_matches']}, runs={row['ipl_runs']}, wkts={row['ipl_wkts']})")
    except Exception as e:
        print(f"{name}: FAILED ({str(e)[:100]})")

    time.sleep(1)

with open("data/raw/ipl_stats.json", "w", encoding="utf-8") as f:
    json.dump(all_players, f, indent=2)

print(f"\nTotal players with stats collected: {len(all_players)}")