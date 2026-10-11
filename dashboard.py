import streamlit as st
import pandas as pd
import requests
import time

st.set_page_config(page_title="Real-Time Analytics Dashboard", layout="wide")
st.title("🚀 Real-Time Telemetry Data Pipeline")

try:
    response = requests.get("http://127.0.0.1:8000/latest")
    data_stream = response.json()
except Exception:
    data_stream = []

if len(data_stream) > 0:
    df = pd.DataFrame(data_stream)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Live Speed Monitoring")
        st.line_chart(df, x="timestamp", y="speed")
    with col2:
        st.subheader("Live Temperature Monitoring")
        st.line_chart(df, x="timestamp", y="temperature")
        
    st.subheader("Latest Raw Telemetry Stream")
    st.dataframe(df.tail(10))
else:
    st.info("Waiting for data stream... Make sure your backend and producer scripts are running!")

time.sleep(1)
st.rerun()