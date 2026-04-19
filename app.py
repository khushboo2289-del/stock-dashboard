import streamlit as st
from data_fetch import fetch_data
from scoring import calculate_scores

st.title("📊 Stock Dashboard")

@st.cache_data
def load_data():
    data = fetch_data()
    data = calculate_scores(data)
    return data

df = load_data()

# ✅ Safe display
if df is None or df.empty:
    st.warning("No data available. Try refreshing.")
else:
    st.dataframe(df)
