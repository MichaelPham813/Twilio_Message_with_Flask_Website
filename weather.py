from urllib import request
import json
import os
#Variable
CITY = "Sudbury"
API_KEY = os.environ['WEATHER_API_KEY']
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"


#Weather function and convert temperature
def weather():
    access = request.urlopen(URL)
    response = json.load(access)
    return f"The temperature in {CITY} is {round(response['main']['temp']-273.15)} C degree"
