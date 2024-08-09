import streamlit as st
st.markdown("""
# Read Me
This is a simple application to demonstrate streamlit functionality. 
The application was originally designed to pull data from a PostgreSQL database
but has been converted to using datasources from CSV files in the data directory.

## About Data
All of the data used in this application is randomly generated.

## Purpose
The Radio Check-in dashboard is designed around the concept of a residential radio network.
It assumes that all members of the network should do a radio check on a specific day each month.
In addition, it assumes there is a primary point of contact or Net Control Operator that receives each check in and documents the quality of the call. 
That data is compiled in a database and the dashboard helps to identify potential network problems.
Network problems could be members of the network that don't do the radio check (**No Attempt**), couldn't complete the check (**Failed**), or a potential technical issue (**Broken and Unreadable**).
""")