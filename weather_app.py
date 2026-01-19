from config import Config
from services.Openeather_api import fetch_weather
import time
from services.exel_files import save_to_excel,read_excel_file
from config import Config
while True:
    weather = fetch_weather()
    print("test")
    # save_to_excel(weather, Config.XLSX_PATH)
    # time.sleep(5)
    # read_excel_file(Config.XLSX_PATH)
    if weather:
        print(f"Data pomiaru: {weather['data_pomiaru']}")
        print(f"Miasto: {weather['miasto']}")
        print(f"Temperatura: {weather['temperatura']} °C")
        print(f"Odczuwalna: {weather['odczuwalna_temperatura']} °C")
        print(f"Wilgotność: {weather['wilgotność']} %")
        print(f"Ciśnienie: {weather['ciśnienie']} hPa")
        print(f"Wiatr: {weather['wiatr']} m/s")
        time.sleep(60)