import requests
from urllib.parse import quote_plus

def get_lat_long(address):
    """
    Fetch latitude and longitude for a given address using the Nominatim API.
    Ensures proper formatting and handles edge cases.
    """
    # Trim leading/trailing whitespace and ensure proper formatting
    address = address.strip()

    # Validate city/state format (only letters, spaces, and commas allowed)
    if not all(c.isalpha() or c.isspace() or c == ',' for c in address):
        print("Invalid city/state format. Only letters, spaces, and commas are allowed.")
        return None, None

    # URL encode the address to handle spaces correctly (e.g., "San Francisco" -> "San+Francisco")
    encoded_address = quote_plus(address)
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
city = 'San Francisco'
state = 'California'
latitude, longitude = get_lat_long(f"{city}, {state}")

if latitude and longitude:
    print(f'The latitude and longitude of {city}, {state} are {latitude}, {longitude}.')
else:
    print(f'Could not find the latitude and longitude for {city}, {state}.')




