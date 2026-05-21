import streamlit as st

st.title("My First Streamlit App")

st.header("About Me")

st.write("Hey Everyone 👋, I am Arun Jawlia")

st.markdown("I am Learning Streamlit Day-2")

code = '''
def displayMyName(name):
    return f"hello my name is {name}"

'''

st.code(code, language="Arun")

student = {
    "name": "Arun",
    "skills": ["Python", "Django","Streamlit", "ReactJs", "JavaScript", "Nodejs", "MicroServices"]
}

st.json(student)