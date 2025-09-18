import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")

model = joblib.load("model.pkl")

with st.form("predict"):
    rent = st.number_input("Monthly Rent", value=15000)
    sqft = st.number_input("Square Feet", value=1000)
    locality = st.text_input("Locality (e.g., Downtown)", "Downtown")
    bedrooms = st.number_input("Bedrooms", value=2, min_value=0, max_value=10, step=1)
    parking = st.text_input("Parking (Open/Covered/Missing)", "Open")
    submitted = st.form_submit_button("Predict")

if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "sqft": sqft,
        "locality": locality if locality else "Missing",
        "bedrooms": bedrooms,
        "parking": parking if parking else "Missing"
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
