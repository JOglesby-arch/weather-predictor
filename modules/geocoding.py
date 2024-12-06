import requests
from urllib.parse import quote_plus

def get_lat_long(address):
    """
    Fetch latitude and longitude for a given address using the Nominatim API.
    """
    # URL encode the address and ensure we're querying for USA explicitly
    encoded_address = quote_plus(address + ", USA")  # Ensure the address has ", USA"
    print(f"Querying geocoding API with address: {encoded_address}")  # Debugging output
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={encoded_address}"

    try:
        response = requests.get(url, headers={'User-Agent': 'WeatherApp'})
        response.raise_for_status()  # Check for request errors (e.g., 4xx, 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None, None

    data = response.json()

    if not data:
        print(f"No data found for {address}")
        return None, None

    # Debugging: print the full response data for inspection
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
city = 'Milwaukee'
state = 'Wisconsin'
latitude, longitude = get_lat_long(f"{city}, {state}")

if latitude and longitude:
    print(f'The latitude and longitude of {city}, {state} are {latitude}, {longitude}.')
else:
    print(f'Could not find the latitude and longitude for {city}, {state}.')


