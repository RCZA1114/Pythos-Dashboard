import streamlit as st

selected_measurement = st.selectbox('Select Measurement', ('PM2.5', 'Humidity', 'Temperature', 'VOC', 'Pressure'))
