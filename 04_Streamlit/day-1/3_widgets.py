import streamlit as st

st.title("User Input Widgets")

# Text Input
name = st.text_input("Enter Your Name")

# Number Input
age = st.number_input(
    "Enter Your Age",
    min_value=1,
    max_value=100
)

# Selectbox
language = st.selectbox(
    "Favorite Language",
    ["Python", "Java", "C++", "JavaScript"]
)

# Multiselect
skills = st.multiselect(
    "Select Skills ( MultiSelect )",
    ["Python", "HTML", "CSS", "SQL"]
)

# Slider
experience = st.slider(
    "Years of Experience",
    0,
    10
)

# Checkbox
agree = st.checkbox("Accept Terms")

# Button
if st.button("Submit"):

    st.success("Form Submitted")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Language:", language)
    st.write("Skills:", skills)
    st.write("Experience:", experience)
    st.write("Accepted:", agree)