# Basic Streamlit App

import streamlit as st

st.title("Welcome to Streamlit")

user_name = st.text_input("Enter Your Name: ")
st.write(user_name)

greet_btn = st.button('Greet Me')

if greet_btn:
    st.write("Hello !")