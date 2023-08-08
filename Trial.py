import streamlit as st
from data import *

placeholder = st.empty()

data = pd.DataFrame(sql_query, columns=['tower_id', 'pm2_5', 'humidity', 'temp', 'voc', 'pressure', 'last_update'])

data['last_update'] = pd.to_datetime(data['last_update'])

data.rename(
    columns={"tower_id": "Tower ID", "pm2_5": "PM2.5", "voc": "VOC", "humidity": "Humidity", "temp": "Temperature",
                "pressure": "Pressure", "last_update": "Date/Time"},
    inplace=True,
    )

data = data.replace({'Tower ID': {'T0703220001': 'Tower 1', 'T0703220002': 'Tower 2', 'T0703220005': 'Tower 5',
                                      'T0703220006': 'Tower 6', 'T0703220008': 'Tower 8', 'T0703220009': 'Tower 9'}})

st.markdown("### Detailed Data View")
st.dataframe(data)


