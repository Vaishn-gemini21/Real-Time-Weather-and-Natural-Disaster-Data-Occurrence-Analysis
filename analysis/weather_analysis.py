class WeatherAnalysis:
    def compare_tempaeratures(self,temp_today,temp_yesterday):
        """
        Compare today's temperautre with yesterday's temperature.
        """
        difference  = temp_today - temp_yesterday

        if difference > 0:
            return f"Today is {difference : .1f}°C warmer than yesterday."
        elif difference < 0:
            return f"Today is {abs(difference):1.f}°C cooler than yesterday."
        else:
            return "Temperature is same as yesterday."
        
    def humidity_advice(self, humidity):
        """
        Provide information on the level of humidity.

        """

        if humidity < 30 :
            return "Air is very dry. You might feel dehydrated."
        elif 30 <= humidity <= 60 :
            return "Humidity is comfortable."
        else:
            return "HIgh humidity. Feels Sticky & uncomfortable."
    
    def detect_weather_condition (self, weather_desc):
        """
        Interpret API Weather descriptions (like 'rain',  'clear' ,etc)

        """
        
        weather_desc = weather_desc.lower()

        if "rain" in weather_desc:
            return "It is raining ! Carry and umberella"
        elif "cloud" in weather_desc:
            return "Cloudy skies expected."
        if "clear" in weather_desc:
            return "Clear skies — a pleasant day."
        if "storm" in weather_desc or "thunder" in weather_desc:
            return "Thunderstorm warning — be cautious."
        if "snow" in weather_desc:
            return "Snowfall expected — stay warm."

        return "Weather looks normal today."
    
    def wind_speed_category(self,wind_speed):
        """
        Categorize wind levels 

        """

        if wind_speed < 2:
            return "Calm Winds"
        elif 2 <= wind_speed <= 10:
            return "Light Breeze"
        if 10 < wind_speed < 20 :
            return "Windy"
        else :
            return "Strong winds_secure loose objects"
        
