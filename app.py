{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
from data_fetch import fetch_data\
from scoring import calculate_scores\
\
st.title("\uc0\u55357 \u56522  Stock Dashboard")\
\
if st.button("Refresh Data"):\
    st.cache_data.clear()\
\
@st.cache_data\
def load_data():\
    data = fetch_data()\
    data = calculate_scores(data)\
    return data\
\
df = load_data()\
\
st.dataframe(df)}