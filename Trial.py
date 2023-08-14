import streamlit as st
from definitions import definitions

selected_measurement = st.selectbox('Select Measurement', ('PM2.5', 'Humidity', 'Temperature', 'VOC', 'Pressure'))


for d in dictionaries:
  if d == selected_measurement:

    st.write(f"This is {selected_measurement[d]}")
