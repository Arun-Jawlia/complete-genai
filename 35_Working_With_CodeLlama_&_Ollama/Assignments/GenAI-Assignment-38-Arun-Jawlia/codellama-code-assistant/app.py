#pylint: disable = all

import streamlit as st
from assistant import (
    generate_code,
    generate_code_bug_fixing,
    generate_code_explanation,
    generate_code_optimization_suggestion,
)

st.title("CodeLlama AI Coding Assistant")

user_input = st.text_area("Enter your code or prompt", height=200)

task = st.selectbox('Choose Task', ['Generate Code', 'Explain Code', 'Debug my code', 'Optimize the code'])

if st.button("Run"):

    if task == "Generate Code":
        output = generate_code(user_input)

    elif task == "Explain Code":
        output = generate_code_explanation(user_input)

    elif task == "Debug Code":
        output = generate_code_bug_fixing(user_input)

    elif task == "Optimize Code":
        output = generate_code_optimization_suggestion(user_input)

    st.subheader("Result")

    st.code(output)