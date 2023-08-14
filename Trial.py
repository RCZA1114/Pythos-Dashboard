import streamlit as st
from definitions import definitions

selected_measurement = st.selectbox('Select Measurement', ('PM2.5', 'Humidity', 'Temperature', 'VOC', 'Pressure'))

x = selected measurement

st.write(f"This is {x}")
