import requests
from urllib.parse import quote_plus

def get_lat_long(address):
    """
    Fetch latitude and longitude for a given address using the Nominatim API.
    """
    # Encode the address to ensure it's URL-friendly
    encoded_address = quote_plus(address + ", USA")  # Ensure that USA is part of the address
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={encoded_address}"
    
    try:
        response = requests.get(url, headers={'User-Agent': 'WeatherApp'})
        response.raise_for_status()  # Raise an HTTPError if the response code is not 200
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None, None
    
    data = response.json()

    if not data:
        print(f"No data found for {address}")
        return None, None

    # Print the response data for debugging purposes
    print(f"Geocoding API Response: {data}")

    # Extract latitude and longitude from the first result
    latitude = data[0].get('lat')
    longitude = data[0].get('lon')

    # If latitude and longitude are found, return them
    if latitude and longitude:
        return latitude, longitude
    else:
        print(f"Latitude and Longitude not found for {address}.")
        return None, None

# Example usage:
city = 'Ames'
state = 'Iowa'
latitude, longitude = get_lat_long(f"{city}, {state}")

if latitude and longitude:
    print(f'The latitude and longitude of {city}, {state} are {latitude}, {longitude}.')
else:
    print(f'Could not find the latitude and longitude for {city}, {state}.')