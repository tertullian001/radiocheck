import streamlit as st
from st_pages import get_nav_from_toml
st.set_page_config(layout="wide")
st.title("Radio Check-in Tracker")
nav = get_nav_from_toml("pages_sections.toml")
pg = st.navigation(nav)
pg.run()
