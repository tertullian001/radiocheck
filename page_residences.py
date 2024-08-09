import streamlit as st
import pandas as pd

df_residence = pd.read_csv("data/residences.csv")
df_residence['latitude'] = df_residence['latitude'].astype(float)
df_residence['longitude'] = df_residence['longitude'].astype(float)

st.map(df_residence, latitude='latitude', longitude='longitude')
