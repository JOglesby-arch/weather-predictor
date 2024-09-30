# modules/visualization.py

import matplotlib.pyplot as plt
import pandas as pd

def create_summary_table(summary):
    if not summary:
        print("No summary data available.")
        return

    data = {
        "Metric": ["Min Temperature (°C)", "Max Temperature (°C)", "Mean Temperature (°C)"],
        "Value": [summary["min_temperature"], summary["max_temperature"], summary["mean_temperature"]]
    }
    df = pd.DataFrame(data)
    print("\nWeather Summary Table:")
    print(df)

def generate_temperature_plot(weather_data):
    if not weather_data:
        print("No weather data available for plotting.")
        return
    
    times = weather_data["times"]
    temperatures = weather_data["temperatures"]

    # Plotting temperature over time
    plt.figure(figsize=(10, 5))
    plt.plot(times, temperatures, label='Temperature (°C)', color='blue')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Hourly Temperature Forecast')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
