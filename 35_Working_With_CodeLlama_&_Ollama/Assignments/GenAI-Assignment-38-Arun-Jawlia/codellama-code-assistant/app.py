#pylint: disable = all

import streamlit as st
from assistant import (
    code_generation,
    code_explaination,
    code_bug_fixing,
    code_optimization
)

st.title("CodeLlama AI Coding Assistant")

user_input = st.text_area("Enter your code or prompt", height=200)

task = st.selectbox('Choose Task', ['Generate Code', 'Explain Code', 'Debug Code', 'Optimize Code'])

if st.button("Run"):

    if task == "Generate Code":
        output = code_generation(user_input)

    elif task == "Explain Code":
        output = code_explaination(user_input)

    elif task == "Debug Code":
        output = code_bug_fixing(user_input)

    elif task == "Optimize Code":
        output = code_optimization(user_input)

    st.subheader("Result")

    st.code(output)