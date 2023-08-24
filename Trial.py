import streamlit as st
from datetime import timedelta
import plotly.express as px
from data import *
from definitions import definitions

#______________________________SETTING UP THE DATA

st.set_page_config(
    page_title="Pythos Dashboard",
    page_icon="👋",
)


st.title("Pythos Dashboard")


st.sidebar.success("Select a page above.")


st.header("Data for the Day!!!!")
@st.cache_data
def load_data():
    #data = pd.read_csv("2023.csv", usecols=['tower_id', 'pm2_5', 'humidity', 'temp', 'voc', 'pressure', 'date', 'time'])
    data = pd.DataFrame(sql_query, columns=['tower_id', 'pm2_5', 'humidity', 'temp', 'voc', 'pressure','last_update'])


    data['last_update'] = pd.to_datetime(data['last_update'])


    data.rename(
        columns={"tower_id": "Tower ID", "pm2_5": "PM2.5", "voc": "VOC", "humidity": "Humidity", "temp": "Temperature", "pressure": "Pressure", "last_update": "Date/Time"},
        inplace=True,
    )


    data = data.replace({'Tower ID': {'T0703220001': 'Tower 1', 'T0703220002': 'Tower 2', 'T0703220005': 'Tower 5',
                                      'T0703220006': 'Tower 6', 'T0703220008': 'Tower 8', 'T0703220009': 'Tower 9'}})



    return data

    
data = load_data()


date = st.date_input('Input Date')
time = st.time_input('Input Time')


# Filter data
datetime_str = str(date) + ' ' + str(time)
current_datetime = pd.to_datetime(datetime_str)

current_datetime = current_datetime + timedelta(hours=8)
start_datetime = current_datetime - timedelta(hours=24)  # - 24 hours

fifteen = current_datetime - timedelta(minutes=45)

filtered_data = data[(data['Date/Time'] >= start_datetime) & (data['Date/Time'] <= current_datetime)]

filtered_data_2 = data[(data['Date/Time'] >= fifteen) & (data['Date/Time'] <= current_datetime)]

st.dataframe(filtered_data)

st.button("Refresh Data", on_click=load_data())
