# modules/data_processing.py

def parse_weather_data(json_data):
    if json_data is None:
        return None

    # Extract latitude, longitude, and hourly temperature
    latitude = json_data.get("latitude")
    longitude = json_data.get("longitude")
    timezone = json_data.get("timezone")
    times = json_data["hourly"]["time"]
    temperatures = json_data["hourly"]["temperature_2m"]

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
    
    temperatures = weather_data["temperatures"]
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    summary = {
        "min_temperature": min_temp,
        "max_temperature": max_temp,
        "mean_temperature": mean_temp
    }

    return summary
