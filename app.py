import pandas as pd
import streamlit as st
import plotly.express as px

@st.cache
def get_data():
    url = "laptops.csv"
    return pd.read_csv(url)
df = get_data()

