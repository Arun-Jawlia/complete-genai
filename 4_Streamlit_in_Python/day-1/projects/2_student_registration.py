import streamlit as st

st.title("Student Registration Form")

name = st.text_input("Enter Your Name")

email = st.text_input("Enter Your Email")

age = st.number_input("Enter Your Age", min_value = 1, max_value = 100)

gender = st.radio("Select Gender", ["Male", "Female", "Prefer not to say"])

skills = st.multiselect("Select Skills", ["Python", "JavaScript", "SQL", "ReactJs"])

experience = st.slider("How many years of Experience:", 0, 10)

agree = st.checkbox("Accepts Terms")

if st.button("Submit"):
    st.success("Form Submitted Successfully")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
    st.write("Skills:", skills)
    st.write("Experience:", experience)
    st.write("Accepted:", agree)
