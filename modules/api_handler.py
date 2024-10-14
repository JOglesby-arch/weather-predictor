# modules/api_handler.py

import requests

def get_weather_data(location, days):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location['latitude'],
        "longitude": location['longitude'],
        "hourly": "temperature_2m",
        "forecast_days": days
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()  # Parse the response to JSON
    else:
        print("Failed to retrieve data:", response.status_code)
        return None
