
import streamlit as st
import yfinance as yf
from src.pattern_detector import detect_cup_and_handle

st.title("📊 NSE Cup & Handle Pattern Scanner")

symbol = st.text_input("Enter NSE Stock Symbol (with .NS)", value="TCS.NS")

if st.button("Scan"):
    data = yf.download(symbol, interval='5m', period='5d')
    if not data.empty:
        patterns = detect_cup_and_handle(data)
        if not patterns.empty:
            st.success("Patterns detected!")
            st.dataframe(patterns)
        else:
            st.info("No patterns found in the selected period.")
    else:
        st.error("Failed to fetch data for the provided symbol.")
