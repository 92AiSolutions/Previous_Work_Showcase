import streamlit as st
import pandas as pd

df = pd.read_csv("data.csv")

st.title("Sales Dashboard")

category = st.selectbox("Select Category", df["Category"].unique())
filtered = df[df["Category"] == category]

st.bar_chart(filtered["Sales"])
