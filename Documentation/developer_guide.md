# Developer's Documentation for Weather Prediction App

## 1. **Overview**

The Weather Prediction App is designed to provide weather forecasts based on user input for a city and state. The app fetches data from Open-Meteo API and displays weather summaries and alerts. The app features an interactive temperature plot using **Plotly** and visualizes the summary data using **Streamlit**.

The app is designed with modularity in mind, splitting functionality across different modules such as **geocoding**, **API handling**, **data processing**, and **visualization**.

## 2. **Condensed Version of the Planning Specs**

### Implemented Features:
- **Weather Data Retrieval**: The app fetches weather data using the Open-Meteo API, including temperature forecasts.
- **Geocoding**: The app uses the Nominatim API to fetch latitude and longitude based on city and state input.
- **Weather Alerts**: The app fetches active weather alerts based on the UGC code from the National Weather Service API.
- **Visualization**: Interactive temperature plots are displayed using **Plotly** in the Streamlit app.
  
### Pending Features:
- **User Authentication**: Not implemented yet.
- **Mobile Responsiveness**: While the app works well on desktops, mobile responsiveness has not been optimized.

## 3. **Install / Deployment / Admin Issues**

### Prerequisites:
1. Install **Python 3.x** (preferably Python 3.8 or later).
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt

### Running the App:
- Main entry file: Navigate to the project directory and run the main.py file: 
    python main.py
- Streamlit Interface: The app uses Streamlit for the user interface. To run the app with Streamlit, use the following command:
    streamlit run main.py

## 4. **User Interaction and Flow Through the Code**

### User Flow:
1. The user enters a **city** and **state** into the text input fields.
2. The **geocoding module** fetches the latitude and longitude based on the city and state.
3. The **weather data** is fetched from the Open-Meteo API using the coordinates.
4. The weather data is processed and displayed as a **summary table**.
5. A **temperature plot** is generated using **Plotly** and displayed.
6. **Weather alerts** (if available) are shown for the specified location.

### Code Walkthrough:
- **Geocoding** (`get_lat_long`): Converts city/state input into geographical coordinates using the Nominatim API.
- **Weather Data Retrieval** (`get_weather_data`): Fetches hourly temperature data from Open-Meteo.
- **Data Processing** (`parse_weather_data`): Parses the raw data returned by the API into a usable format.
- **Visualization** (`generate_temperature_plot`): Generates a temperature plot using **Plotly** and displays it in the **Streamlit** interface.

## 5. **Known Issues**

### Minor:
- **Geocoding**: Some cities with ambiguous names (e.g., **Chicago**) may not be parsed correctly, returning an inaccurate result.
- **Weather Data**: The app sometimes fails to fetch data if the **Open-Meteo API** is down or slow.

### Major:
- **Geocoding Failure for Certain Locations**: Occasionally, the geocoding API may fail to return latitude and longitude for certain cities or regions.
- **API Rate Limits**: The app may hit API rate limits if too many requests are made in a short period.

### Other:
- **Optimization for Larger Data Sets**: The app may experience slower response times when fetching weather data for a large number of days or a large number of users.

## 6. **Future Work**

1. **Support for More APIs**: Integrate additional weather APIs (e.g., **AccuWeather**, **WeatherStack**) for more detailed weather information.
2. **User Authentication**: Implement user login and preferences to allow users to save their favorite locations.
3. **Improve Error Handling**: Add better error handling for missing or invalid inputs and better user feedback.
4. **Mobile Responsiveness**: Ensure the app is optimized for mobile screens.

## 7. **Conclusion**

The Weather Prediction App is a functional and interactive tool that provides users with real-time weather forecasts based on their city and state input. By integrating several APIs, including Open-Meteo for weather data, Nominatim for geocoding, and National Weather Service for weather alerts, the app delivers accurate and relevant weather information with an intuitive user interface built using Streamlit.

In this version of the app, key features such as weather data retrieval, geocoding, weather alerts, and visualization have been successfully implemented. The app provides users with a simple way to view weather predictions, while Plotly ensures that the data is presented in an interactive and easily interpretable format.