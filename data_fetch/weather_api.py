import requests
import os
 
class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city):
        try:
            params = {
                "q" : city,
                "appid" : self.api_key,
                "units": "metric"
            }
            response = requests.get(self.base, params=params)
            response.raise_for_status()
            data = response.json()
        
            return {
                "city" : city ,
                "temperature" : data["main"]["temp"],
                "humidity" : data["main"]["humidity"],
                "pressure" : data["main"]["pressure"],
                "weather" : data["weather"][0]["description"],
                "wind_speed" : data["wind"]["speed"]
            }
        except Exception as e:
            print("Error fetching weather :", e)
            return None
        





