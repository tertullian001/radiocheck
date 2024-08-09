import streamlit as st
import pandas as pd

df_checkin = pd.read_csv('data/checkin.csv')
df_checkin['checkin_on'] = pd.to_datetime(df_checkin['checkin_on'])
df_checkin['latitude'] = df_checkin['latitude'].astype(float)
df_checkin['longitude'] = df_checkin['longitude'].astype(float)


def df_color_value(quality):
    if quality == "Loud and Clear":
        return '#64ff33'
    elif quality == "Broken but Readable":
        return '#00fff3'
    elif quality == "Broken and Unreadable":
        return '#ffa200'
    elif quality == "No Attempt":
        return '#c8c8c8'
    elif quality == "Failed":
        return '#ff0000'
    else:
        return '#000000'


df_checkin['color'] = df_checkin['quality'].apply(df_color_value)

# Print the dataframe to streamlit
st.write(df_checkin)
