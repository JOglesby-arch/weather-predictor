# modules/alerts_handler.py

import requests

def fetch_weather_alerts(ugc_code):
    """
    Fetch active weather alerts based on the provided UGC code.
    
    Args:
        ugc_code (str): The UGC code for the geographical zone.
        
    Returns:
        list: A list of active weather alerts or an empty list if no alerts are found.
    """
    url = f"https://api.weather.gov/zones/forecast/{ugc_code}"
    response = requests.get(url)
    
    if response.status_code == 200:
        zone_info = response.json()
        alerts = zone_info.get('alerts', [])
        return alerts
    else:
        print("Failed to retrieve alerts:", response.status_code)
        return []
