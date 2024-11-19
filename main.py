import streamlit as st
from modules.api_handler import get_weather_data
from modules.data_processing import parse_weather_data, calculate_summary
from modules.visualization import create_summary_table, generate_temperature_plot
from modules.geocoding import get_lat_long
from modules.alerts_handler import fetch_weather_alerts
import requests

def get_ugc_code(lat, lon):
    """
    Fetch UGC code based on latitude and longitude.
    """
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
    city = st.text_input("Enter the city name:")
    state = st.text_input("Enter the state name:")

    if city and state:
        # Get coordinates for the city and state
        latitude, longitude = get_lat_long(f"{city}, {state}, USA")
        
        if latitude and longitude:
            st.write(f"The latitude and longitude of {city}, {state} are {latitude}, {longitude}.")

            # Ask the user for the number of forecast days
            days = st.slider("Select the number of days to forecast", 1, 16, 7)  # Default to 7 days

            # Fetch weather data
            location = {"latitude": float(latitude), "longitude": float(longitude)}  # Prepare the location dictionary
            weather_data = get_weather_data(location, days)
            
            if weather_data:
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
                if parsed_data:
                    summary = calculate_summary(parsed_data)

                    # Generate and display output
                    create_summary_table(summary)
                    
                    # Generate the Plotly temperature plot and display it with Streamlit
                    generate_temperature_plot(parsed_data)
                else:
                    st.error("Failed to parse weather data.")
            else:
                st.error("Failed to retrieve weather data. Please try again.")
        else:
            st.error("Could not get coordinates for the provided city and state.")
    else:
        st.warning("Please enter both city and state.")

if __name__ == "__main__":
    main()
