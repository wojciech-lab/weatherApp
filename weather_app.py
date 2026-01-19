from config import Config
from services.Openeather_api import fetch_weather
import time


while True:
    weather = fetch_weather()
    print("test")
    if weather:
        print(f"Data pomiaru: {weather['data_pomiaru']}")
        print(f"Miasto: {weather['miasto']}")
        print(f"Temperatura: {weather['temperatura']} °C")
        print(f"Odczuwalna: {weather['odczuwalna_temperatura']} °C")
        print(f"Wilgotność: {weather['wilgotność']} %")
        print(f"Ciśnienie: {weather['ciśnienie']} hPa")
        print(f"Wiatr: {weather['wiatr']} m/s")