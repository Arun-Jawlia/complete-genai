#pylint: disable = all

from langchain_ollama import ChatOllama
from prompts_helper import (
    code_explanation_prompt,
    code_generation_prompt,
    code_optimization_prompt,
    code_bug_fixing_prompt
)

def generate_response(prompt):
    llm = ChatOllama(
        model='codellama:latest',
        temperature=0.5
    )

    response = llm.invoke(prompt)
    return response.content

def code_generation(prompt):
    prompt = code_generation_prompt.format(input = prompt)

    return generate_response(prompt)


def code_explaination(code):
    prompt = code_explanation_prompt.format(code = code)
    return generate_response(prompt)

def code_bug_fixing(code):
    prompt = code_bug_fixing_prompt.format(code=code)

    return generate_response(prompt)


def code_optimization(code):
    prompt = code_optimization_prompt.format(code=code)
    return generate_response(prompt)
