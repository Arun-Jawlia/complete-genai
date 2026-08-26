#pylint:disable = all

from langchain_core.prompts import PromptTemplate

code_generation_prompt = PromptTemplate(
    template= """
    You are a Python Programming expert.
    Generate clean and readable Python code for the following prompt
    Input: {input}
""",
input_variables=['input']
)

code_explanation_prompt = PromptTemplate(
    template="""
    Acts a PYthon Instructor.
    Explain the following Python Code.
    Code: {code}
""",
input_variables=['code']
)



code_bug_fixing_prompt = PromptTemplate(
    template="""
    You are a senior Python developer.
    Analyze the following Python code for bugs.
    Code:{code}

    Provide:
    1. The bug
    2. Why it happens
    3. Correct  Code
""",
    input_variables=["code"]
)

code_optimization_prompt = PromptTemplate(
    template="""
    You are a Python expert.
    Review the following Python code.

    Code:{code}

    Provide:
    1. Problems in the current code implementation
    2. An improved version
    3. Give me reason why the new version is better
""",
input_variables=["code"],
)
