import requests
from dotenv import load_dotenv
import os

load_dotenv()

city = os.getenv("CITY","Phnom Penh")

print(f"Weather for {city}")

res = requests.get(
    "https://wttr.in",
)

print(res.text)