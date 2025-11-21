from data_fetch.weather_api import WeatherAPI
from analysis.weather_analysis import WeatherAnalysis
from visualization.charts import ChartVisualizer
from Static_model.old_code import run_old_code
import config

def run_realtime_system():
    weather = WeatherAPI(config.OPENWEATHER_API_KEY)
    analyzer = WeatherAnalysis()
    visual = ChartVisualizer()

    city = input("Enter city name: ")
    data = weather.get_weather(city)

    if data:
        print("\n--- Current Weather Report ---")
        print(f"City: {data['city']}")
        print(f"Temperature: {data['temperature']}°C")
        print(f"Humidity: {data['humidity']}%")
        print(f"Pressure: {data['pressure']} hPa")
        print(f"Weather: {data['weather']}")
        print(f"Wind Speed: {data['wind_speed']} m/s")

        print("\n--- Analysis ---")
        print(analyzer.humidity_advice(data["humidity"]))
        print(analyzer.detect_weather_condition(data["weather"]))
        print(analyzer.wind_speed_category(data["wind_speed"]))

        print("\nChoose the type of graph : ")
        print("1. Line Graph")
        print("2. Bar Graph")
        print("3. Pie Chart")

        graph_choice = int(input("Enter the choice: "))

        labels=["Temperature", "Humidity", "Wind Speed"]
        values = [data["temperature"], data["humidity"], data["wind_speed"]]

        if graph_choice == 1:
            visual.plot_line(
                x = labels,
                y = values,
                title= "Weather Parameters",
                xlabel="Parameters",
                ylabel="Values"
            )
    
        elif graph_choice == 2:
            visual.plot_bar(
                labels = labels,
                values = values,
                title= "Weather Report",
                xlabel="Parameters",
                ylabel="Values"
            )
    
        elif graph_choice == 3:
            visual.plot_pie(
                labels = labels,
                values = values,
                title= "Weather Composition",
            )

        else:
            print("Invalid Choice.")
    else:
        print("Unable to fetch real-time data")

def main():
    weather = WeatherAPI(config.OPENWEATHER_API_KEY)

    print("\n====WEATHER & NATURAL DISASTER ANALYSIS SYSTEM===\n")
    print("1. Real-Time Weather (API)")
    print("2. Historical Weather Data (Static CSV Model)")
    print("3. Exit")

    choice = int(input("Enter the choice : "))

    if choice == 1:
        run_realtime_system()
    elif choice == 2:
        run_old_code()
    elif choice == 3:
        print("Exiting...")
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()












