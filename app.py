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
                st.subheader("Active Weather Alerts")
                for alert in alerts:
                    st.write(f"**Title**: {alert['title']}")
                    st.write(f"**Severity**: {alert['severity']}")
                    st.write(f"**Area**: {alert['area']}")
                    st.write(f"**Description**: {alert['description']}")
                    st.write(f"**Effective**: {alert['effective']}")
                    st.write(f"**Expires**: {alert['expires']}")

            # Process and display weather data (implement your display logic here)
        else:
            st.error(f"Could not get coordinates for {city}, {state}. Please try again.")

if __name__ == "__main__":
    main()
