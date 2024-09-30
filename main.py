from modules.api_handler import get_weather_data
from modules.data_processing import parse_weather_data, calculate_summary
from modules.visualization import create_summary_table, generate_temperature_plot

def main():
    # Welcome message
    print("Welcome to the Weather Prediction App!")

    # Get user input
    location = input("Enter the location (e.g., latitude,longitude - '52.52,13.419'): ")
    latitude, longitude = [float(coord) for coord in location.split(",")]
    days = int(input("Enter number of days to forecast (1-16): "))

    # Fetch weather data
    weather_data = get_weather_data({"latitude": latitude, "longitude": longitude}, days)
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
