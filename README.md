## User's Guide for Weather Prediction App

## 1. **Prerequisites**
Before you can run the app, ensure that you have:
- **Python 3.8+** installed on your machine.
- **API key for the National Weather Service** (if you plan to fetch weather alerts).

## 2. **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-predictor.git

2. Install dependencies:
    pip install -r requirements.txt

## 3. **Setting Up API Keys (if applicable)**

1. **Open-Meteo (No API Key Required)**
    - Open-Meteo does not require an API key, so you don’t need to set up anything for this API.

2. **National Weather Service API (Requires API Key)**
    - No key required for the National Weather Service API, but you will need the UGC code for your location. This code will be dynamically retrieved based on the city/state you provide.

## 4. **Running the App**

Once everything is isntalled and set up, you may run the app!

**Main Entry Point**
    - Run app using Streamlit
        streamlit run main.py
    - This will open a local server, and you can access the app through you browser at *http://localhost:8501.*

**Interacting with the App**

1. **Enter a city and state**:

    - Use the input fields to type the name of the city and state (e.g., Ames, Iowa).
    - The app will use the Nominatim geocoding API to find the latitude and longitude for the city/state you enter.

2. **Select the number of forecast days**:

    - Use the slider to select how many days of the forecast you want (1–16 days). The default is 7 days.

3. **View weather data**:

    - Once the location and forecast days are selected, the app will fetch the weather data (temperature) for the selected number of days from Open-Meteo.
    - A summary table of the weather data will be displayed.
    - An interactive temperature plot will be generated using Plotly.

4. **Weather Alerts**:

    - If available, weather alerts for your location will be displayed, including details like title, severity, description, and expiration time.

## 5. **Common Errors and How to Fix Them**

While running the app, you might encounter a few common errors. Below are some of the potential issues and their solutions:

**Invalid City/State**:
- If you enter a city/state that can't be found or is misspelled, the app will display an error message:
    - "Could not get coordinates for the provided city and state."
    - **Solution**: Double-check the spelling and ensure you're entering a valid city/state combination.

**API Failures**:
- Sometimes the weather data or weather alerts might not be retrieved due to external API failures.
    - "Failed to retrieve weather data."
    - **Solution**: Check if the Open-Meteo API or National Weather Service API is down. You can try again later or check for server issues.

**Streamlit Errors**:
- If Streamlit fails to launch:
    - "Streamlit could not be started."
    - **Solution**: Ensure you’ve installed Streamlit correctly by running *pip install streamlit*


## 6. **Conclusion**

The Weather Prediction App provides an interactive and easy-to-use interface for checking weather forecasts and weather alerts based on city and state inputs. While there are some known limitations, the app offers valuable functionality and can be expanded further in the future.
