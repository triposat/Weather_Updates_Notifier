import requests
import math
import datetime
from plyer import notification
api_key = "88d279a5ff5fcd8e338ab42d94c819c3"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
if __name__ == '__main__':
    while 1:
        dat = datetime.datetime.now().strftime("%d-%m-%y")
        tim = datetime.datetime.now().strftime("%H : %M : %S")
        city_name = input("Please Enter City name: ")
        complete_url = f"{base_url}appid={api_key}&q={city_name}"
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            curr = current_temperature-273.15
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            notification.notify(title=f"Weather Updates\tDate: {dat}\tTime - {tim}", message=f"City: {city_name.capitalize()}\nTemperature: "
                                f"{math.ceil(curr)}{chr(176)}C\nAtmospheric Pressure: {current_pressure} hpa"
                                f"\nHumidity: {current_humidiy}%\nDescription"
                                f": {weather_description}", app_icon="C:/Users/Dell/Downloads/weather.ico", timeout=10)
        else:
            notification.notify(title="Alert! City not "
                                "found", message="Please Try Again!", app_icon="C:/Users/Dell/Downloads/err.ico",
                                timeout=10)
        a = input("Do You Want Check Again: Press[Y/N]").lower()
        if a == 'y':
            continue
        else:
            notification.notify(title="Thank You So Much", message="Hope You Enjoyed",
                                app_icon="C:/Users/Dell/Downloads/thank.ico")
            exit()
