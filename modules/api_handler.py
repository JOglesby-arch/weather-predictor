# modules/api_handler.py
import sys
import os 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from keys import WEATHER_API_KEY

def get_weather_data(location, days):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location['latitude'],
        "longitude": location['longitude'],
        "hourly": "temperature_2m",
        "forecast_days": days,
        "apikey": WEATHER_API_KEY
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()  # Parse the response to JSON
    else:
        print("Failed to retrieve data:", response.status_code)
        return None
