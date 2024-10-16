import requests
from urllib.parse import quote_plus

def get_lat_long(address): # 
    encoded_address = quote_plus(address) # URL encode the address
    url = f"https://nominatim.openstreetmap.org/search?format=json&q={encoded_address}"  # Construct the Nominatim API URL
    response = requests.get(url, headers={'User-Agent': 'Python Geocoding Example'}) # Send the request to the Nominatim API
    data = response.json()
    if data: # Return the first result (if any)
        return data[0].get('lat'), data[0].get('lon')
    else:
        return None, None

city = 'Ames'
state = 'Iowa'
latitude, longitude = get_lat_long(f"{city}, {state}, USA")

if latitude and longitude:
    print(f'The latitude and longitude of {city}, {state} are {latitude}, {longitude}.')
else:
    print(f'Could not find the latitude and longitude for {city}, {state}.')
