# modules/visualization.py

import plotly.express as px
import pandas as pd
import streamlit as st  # Import Streamlit for displaying the plot

def create_summary_table(summary):
    if not summary:
        st.error("No summary data available.")
        return
    
    data = {
        "Metric": ["Min Temperature (°C)", "Max Temperature (°C)", "Mean Temperature (°C)"],
        "Value": [summary["min_temperature"], summary["max_temperature"], summary["mean_temperature"]]
    }
    df = pd.DataFrame(data)
    
    # Display the summary table using Streamlit
    st.subheader("Weather Summary Table")
    st.table(df)

def generate_temperature_plot(weather_data):
    if not weather_data:
        st.error("No weather data available for plotting.")
        return
    
    # Assuming weather_data is a dictionary with 'times' and 'temperatures' keys
    times = weather_data["times"]
    temperatures = weather_data["temperatures"]

    # Creating a DataFrame for Plotly
    df = pd.DataFrame({
        "Time": times,
        "Temperature (°C)": temperatures
    })
    
    # Creating the interactive line plot using Plotly
    fig = px.line(df, x='Time', y='Temperature (°C)', title='Hourly Temperature Forecast')
    
    # Customize the appearance (optional)
    fig.update_layout(
        xaxis_title='Time',
        yaxis_title='Temperature (°C)',
        xaxis_tickangle=45
    )
    
    # Display the plot using Streamlit's built-in method
    st.plotly_chart(fig)


