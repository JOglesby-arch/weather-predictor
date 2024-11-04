# app.py

import streamlit as st
from modules.geocoding import get_lat_long
from modules.api_handler import get_weather_data
from modules.alerts_handler import fetch_weather_alerts

def main():
    st.title("Weather Prediction App")

    # User input for city and state
    city = st.text_input("Enter the city name:")
    state = st.text_input("Enter the state name:")

    if st.button("Get Weather"):
        latitude, longitude = get_lat_long(f"{city}, {state}, USA")
        if latitude and longitude:
            # Fetch weather data and alerts
            location = {"latitude": float(latitude), "longitude": float(longitude)}
            weather_data = get_weather_data(location, days=7)  # Example for 7-day forecast
            ugc_code = "YOUR_UGC_CODE"  # Replace with logic to get UGC code
            alerts = fetch_weather_alerts(ugc_code)

            # Display alerts
            if alerts:
                st.subheader("Weather Alerts")
                for alert in alerts:
                    st.write(alert)

            # Process and display weather data (implement your display logic here)
        else:
            st.error(f"Could not get coordinates for {city}, {state}. Please try again.")

if __name__ == "__main__":
    main()
