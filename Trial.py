import streamlit as st
from definitions import definitions
selected_measurement = st.selectbox('Select Measurement', ('PM2.5', 'Humidity', 'Temperature', 'VOC', 'Pressure'))

for d in definitions:

x = selected_measurement
  if d == x:

    st.write(f"This is {definitions[d]}")
