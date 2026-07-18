import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("CRICAPI_KEY")

url = "https://api.cricapi.com/v1/players"
params = {"apikey": API_KEY, "offset": 0, "search": "Virat Kohli"}

response = requests.get(url, params=params, timeout=15)
print("Status code:", response.status_code)
data = response.json()
print(data)