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

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
quality = ['All', 'Loud and Clear', 'Broken but Readable', 'Broken and Unreadable', 'No Attempt', 'Failed']
col1, col2 = st.columns(2)
selected_month = col1.selectbox(
    "Select a Month",
    months,
    index=0
)
selected_quality = col2.selectbox(
    "Select Quality",
    quality,
    index=0
)
filtered_df = df_checkin[
    (df_checkin['checkin_on'].dt.month == months.index(selected_month) + 1) &
    (selected_quality == "All" or df_checkin['quality'] == selected_quality)
    ]

col1.map(filtered_df, latitude='latitude', longitude='longitude', color='color')

c = col2.container()
c.metric(label="Failed", value=len(filtered_df[filtered_df['quality'] == "Failed"]))
c.metric(label="No Attempt", value=len(filtered_df[filtered_df['quality'] == "No Attempt"]))
c.metric(label="Broken and Unreadable", value=len(filtered_df[filtered_df['quality'] == "Broken and Unreadable"]))
c.metric(label="Broken and Unreadable", value=len(filtered_df[filtered_df['quality'] == "Broken but Readable"]))
c.metric(label="Broken and Unreadable", value=len(filtered_df[filtered_df['quality'] == "Loud and Clear"]))
c.metric(label="Total", value=len(filtered_df))