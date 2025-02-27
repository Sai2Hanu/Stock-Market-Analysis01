import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from datetime import datetime
st.subheader("Future Stock Price Forecast")
# Load saved SARIMAX model
@st.cache_resource
def load_model():
    return joblib.load("/content/linear_regression_aapl.pkl")


model = load_model()
