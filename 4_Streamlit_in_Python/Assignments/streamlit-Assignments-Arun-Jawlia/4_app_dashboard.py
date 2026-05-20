# APP Dasboard 

import streamlit as st

st.title('Simple Sales Dashboard')
st.write("This App Shows Monthly Sales")

selected_month = st.sidebar.selectbox('Select Months',["Jan", "Feb", "Mar", "Apr", "May", "June","July", "Aug", "Sept", "Oct", "Nov", "Dec"])

sales = {
    "Jan": 1200,
    "Feb": 800,
    "Mar": 555,
    "Apr": 1100,
    "May": 1500,
    "June": 1800,
    "July": 6520,
    "Aug": 7820,
    "Sept": 300,
    "Oct": 1050,
    "Nov": 2200,
    "Dec": 52640,
}

st.metric(f"{selected_month} Sales", f"{sales[selected_month]}")

st.header("Sales Chart")
st.bar_chart(list(sales.values()))