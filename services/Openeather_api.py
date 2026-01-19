from config import Config
import requests
from datetime import datetime
from utils.functions import to_celsius
URL= f"https://api.openweathermap.org/data/2.5/weather?q={Config.OPENWEATHER_CITY}&appid={Config.OPENWEATHER_API_KEY}"

def fetch_weather():
    try:
        response = requests.get(URL)
        data = response.json()

        weather_dict = {
            "miasto": data.get("name"),
            "temperatura": to_celsius(data.get("main", {}).get("temp")),
            "odczuwalna_temperatura": to_celsius(data.get("main", {}).get("feels_like")),
            "wilgotność": data.get("main", {}).get("humidity"),
            "ciśnienie": data.get("main", {}).get("pressure"),
            "wiatr": data.get("wind", {}).get("speed"),
            "data_pomiaru": datetime.now().strftime("%Y-%m-%d")
        }

        return weather_dict

    except Exception as e:
        print(e)



