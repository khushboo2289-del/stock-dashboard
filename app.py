import streamlit as st
from data_fetch import fetch_data
from scoring import calculate_scores

st.title("📊 Stock Dashboard")

if st.button("Refresh Data"):
    st.cache_data.clear()

@st.cache_data
def load_data():
    data = fetch_data()
    data = calculate_scores(data)
    return data

df = load_data()

st.dataframe(df)
