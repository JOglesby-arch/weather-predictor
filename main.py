from modules.api_handler import get_weather_data
from modules.data_processing import parse_weather_data, calculate_summary
from modules.visualization import create_summary_table, generate_temperature_plot
from modules.geocoding import get_lat_long
from modules.alerts_handler import fetch_weather_alerts

def main():
    # Welcome message
    print("Welcome to the Weather Prediction App!")

    # Get user input for city and state
    city = input("Enter the city name: ")
    state = input("Enter the state name: ")

    # Get coordinates for the city and state
    latitude, longitude = get_lat_long(f"{city}, {state}, USA")
    if not latitude or not longitude:
        print(f"Could not get coordinates for {city}, {state}. Please try again.")
        return

    # Ask the user for the number of forecast days
    days = int(input("Enter number of days to forecast (1-16): "))

    # Fetch weather data
    location = {"latitude": float(latitude), "longitude": float(longitude)}  # Prepare the location dictionary
    weather_data = get_weather_data(location, days)
    
    # Fetch weather alerts using a UGC code (example code, I'll need to adjust it based on the input)
    ugc_code = "YOUR_UGC_CODE"  # Need to determine the correct UGC code based on location
    alerts = fetch_weather_alerts(ugc_code)
    
    if alerts:
        print("Weather Alerts:")
        for alert in alerts:
            print(alert)  # Customize this based on what information you want to display

    if weather_data:
        # Parse and process data
        parsed_data = parse_weather_data(weather_data)
        if parsed_data:
            summary = calculate_summary(parsed_data)

            # Generate and display output
            create_summary_table(summary)
            generate_temperature_plot(parsed_data)
        else:
            print("Failed to parse weather data.")
    else:
        print("Failed to retrieve weather data. Please try again.")

if __name__ == "__main__":
    main()
