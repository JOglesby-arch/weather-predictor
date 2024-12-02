import streamlit as st
from modules.api_handler import get_weather_data
from modules.data_processing import parse_weather_data, calculate_summary
from modules.visualization import create_summary_table, generate_temperature_plot
from modules.geocoding import get_lat_long
from modules.alerts_handler import fetch_weather_alerts
import requests

def get_city_and_state():
    city = st.text_input("Enter the city name:")
    state = st.text_input("Enter the state name:")

    if not city or not state:
        st.error("City and state cannot be empty.")
        return None, None
    if not city.isalpha() or not state.isalpha():
        st.error("Please enter a valid city and state using letters only.")
        return None, None

    return city, state

def get_forecast_days():
    try:
        days = st.slider("Select the number of days to forecast", 1, 16, 7)  # Default to 7 days
    except ValueError:
        st.error("Invalid input for the number of days. Please enter an integer between 1 and 16.")
        return None
    return days

def get_ugc_code(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(url)
    data = response.json()
    forecast_zone = data['properties']['forecastZone']
    ugc_code = forecast_zone.split('/')[-1]  # Extract UGC code from the forecastZone path
    return ugc_code

def main():
    # Welcome message
    st.title("Weather Prediction App")
    st.write("Welcome to the Weather Prediction App!")

    # Get user input for city and state via Streamlit text inputs
    city, state = get_city_and_state()
    if not city or not state:
        return  # Exit if invalid input

    # Get coordinates for the city and state
    latitude, longitude = get_lat_long(f"{city}, {state}, USA")
    if not latitude or not longitude:
        st.error(f"Could not get coordinates for {city}, {state}. Please check the location and try again.")
        return

    st.write(f"The latitude and longitude of {city}, {state} are {latitude}, {longitude}.")

    # Ask the user for the number of forecast days
    days = get_forecast_days()
    if days is None:
        return  # Exit if invalid input

    # Fetch weather data
    location = {"latitude": float(latitude), "longitude": float(longitude)}  # Prepare the location dictionary
    weather_data = get_weather_data(location, days)
    if weather_data is None:
        st.error("Failed to retrieve weather data. Please try again later.")
        return  # Exit if API call fails

    # Fetch weather alerts using a UGC code
    ugc_code = get_ugc_code(latitude, longitude)
    alerts = fetch_weather_alerts(ugc_code)

    if alerts:
        st.subheader("Weather Alerts:")
        for alert in alerts:
            st.write(f"**Title**: {alert['title']}")
            st.write(f"**Severity**: {alert['severity']}")
            st.write(f"**Area**: {alert['area']}")
            st.write(f"**Description**: {alert['description']}")
            st.write(f"**Effective**: {alert['effective']}")
            st.write(f"**Expires**: {alert['expires']}")
            st.write("---")

    # Parse and process data
    parsed_data = parse_weather_data(weather_data)
    if parsed_data is None:
        st.error("Failed to parse weather data.")
        return  # Exit if parsing fails

    # Calculate the summary statistics
    summary = calculate_summary(parsed_data)

    # Generate and display the summary table and temperature plot
    create_summary_table(summary)
    generate_temperature_plot(parsed_data)

if __name__ == "__main__":
    main()
