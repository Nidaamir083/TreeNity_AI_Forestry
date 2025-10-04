import streamlit as st
import pandas as pd
import joblib

st.title("🌳 Tree Survival Prediction – TreeNity")
st.write("Predict the survival probability of trees using environmental data.")

# Inputs
avg_temp = st.number_input("Average Temperature (°C)", 20, 40, 28)
rainfall = st.number_input("Rainfall (mm)", 50, 300, 150)
soil_type = st.selectbox("Soil Type", ["Sandy (0)", "Loamy (1)", "Clay (2)"])
fire_freq = st.slider("Fire Frequency (per year)", 0, 5, 1)
plant_month = st.slider("Planting Month (1–12)", 1, 12, 6)

if st.button("Predict Survival"):
    st.success("Predicted: Tree is likely to survive ✅ (demo prediction)")
