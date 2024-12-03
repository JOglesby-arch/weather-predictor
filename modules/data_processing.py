# modules/data_processing.py

def parse_weather_data(json_data):
    if json_data is None:
        return None

    # Extract latitude, longitude, and hourly temperature
    latitude = json_data.get("latitude")
    longitude = json_data.get("longitude")
    timezone = json_data.get("timezone")

    # Check if hourly data exists and contains the required keys
    hourly_data = json_data.get("hourly", {})
    times = hourly_data.get("time", [])
    temperatures = hourly_data.get("temperature_2m", [])

    # Handle missing or invalid data
    if not times or not temperatures:
        return None

    # Create a dictionary to hold processed data
    weather_data = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "times": times,
        "temperatures": temperatures,
    }
    
    return weather_data

def calculate_summary(weather_data):
    if not weather_data:
        return None
    
    temperatures = weather_data.get("temperatures", [])
    if not temperatures:
        return None

    min_temp = min(temperatures)
    max_temp = max(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    summary = {
        "min_temperature": min_temp,
        "max_temperature": max_temp,
        "mean_temperature": mean_temp
    }

    return summary

