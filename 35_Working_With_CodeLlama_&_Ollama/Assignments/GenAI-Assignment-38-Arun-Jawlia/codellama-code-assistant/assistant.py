#pylint: disable = all
from ollama import chat

MODEL_NAME = 'codellama:latest'

def generate_response(prompt):
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.message.content


def generate_code(prompt):
    prompt = f"""
    
    Act as a expert Python Developer.

    Task: Generate Python Code

    User Requirement:
    {prompt}

    Instructions:
    - Write Clean Python Code
    - Use meaningful variables names
    - follow best practice
    - include comments only where useful
    - return the complete solution
    
    """

    return generate_response(prompt)

def generate_code_explanation(code):
    prompt = f"""
    
    Act as a expert Python Developer.

    Task: Explain the following code in Simple English Language

    Code:
    {code}
    
    """

    return generate_response(prompt)

def generate_code_bug_fixing(code):
    prompt = f"""
    
    Act as a expert Python Developer.

    Task: 
    - Find the bugs in the following code
    - Explain the issue
    - Provide Corrected Code

    Code:
    {code}
    """

    return generate_response(prompt)

def generate_code_optimization_suggestion(code):
    prompt = f"""
    
    Act as a expert Python Developer.

    Task: 
    - Optimize the Code
    - Improve Readibility
    - Improver performance
    - Return Optimized code

    Code:
    {code}
    """

    return generate_response(prompt)


