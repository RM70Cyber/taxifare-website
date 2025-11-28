import streamlit as st
from datetime import datetime
import requests

st.title("TaxiFareModel — Predict your fare")

#pickup_datetime = st.datetime_input("Pickup date and time", value=datetime.now())
date = st.date_input("Pickup date")
time = st.time_input("Pickup time")
pickup_datetime = datetime.combine(date, time)

pickup_longitude = st.number_input("Pickup longitude", value=-73.985428)
pickup_latitude  = st.number_input("Pickup latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff longitude", value=-73.985428)
dropoff_latitude  = st.number_input("Dropoff latitude", value=40.748817)
passenger_count = st.number_input("Number of passengers", min_value=1, max_value=6, value=1)

params = {
    "pickup_datetime": pickup_datetime.strftime("%Y-%m-%d %H:%M:%S"),
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

if st.button("Predict fare"):
    url = "https://taxifare.lewagon.ai/predict"
    response = requests.get(url, params=params)

    if response.status_code == 200:
        prediction = response.json()["fare"]
        st.success(f"Predicted fare: ${prediction:.2f}")
    else:
        st.error("Error calling the API")
