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

    try:
        response = requests.get(base_url, params=params)
        # Check if the response status is OK (200)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return None
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
        return None
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something went wrong: {err}")
        return None

    # Check if the response contains valid JSON data
    try:
        weather_data = response.json()
        if 'hourly' not in weather_data:
            print("Weather data is missing 'hourly' information.")
            return None
        return weather_data
    except ValueError:
        print("Error parsing JSON response.")
        return None
