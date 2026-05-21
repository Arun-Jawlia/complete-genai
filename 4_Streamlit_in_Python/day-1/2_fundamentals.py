import streamlit as st

# Title
st.title("Streamlit Fundamentals")

# Header
st.header("Basic Output Functions")

# Text
st.text("This is simple text")

# Write
st.write("Hello from Streamlit, it is like print statement")

# Markdown
st.markdown("**This is bold**")

# Code
code = '''
def add(a, b):
    return a + b
'''

st.code(code, language="python")

# JSON
student = {
    "name": "Arun",
    "age": 22
}

st.json(student)