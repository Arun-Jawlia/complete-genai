# CodeLlama AI Coding Assistant

A simple local AI coding assistant built with **CodeLlama, Ollama, Python, and Streamlit**.

The application can:

* Generate Python code
* Explain code
* Debug code
* Optimize code

## Tech Stack

* Python
* Ollama
* CodeLlama 7B
* Streamlit

## Project Structure

```text
CodeLlama_Assignment/
│
├── app.py
├── assistant.py
├── prompts.py
├── requirements.txt
└── README.md
```

## Prerequisites

Make sure you have:

* Python installed
* Ollama installed


## How It Works

```text
User Input
    ↓
Streamlit UI
    ↓
Prompt Template
    ↓
Ollama
    ↓
CodeLlama 7B
    ↓
Generated Response
    ↓
Streamlit UI
```

## Available Tasks

### Generate Code

Enter a programming requirement and CodeLlama generates Python code.

### Explain Code

Enter Python code and the assistant explains what the code does.

### Debug Code

Enter code containing an error and the assistant identifies the problem and suggests a correction.

### Optimize Code

Enter existing code and the assistant suggests improvements for readability and performance.

## Example

**Prompt:**

```text
Write a Python function to check whether a number is prime.
```

**Task:**

```text
Generate Code
```

The application sends the prompt to CodeLlama through Ollama and displays the generated response.

## Note

This project runs CodeLlama **locally through Ollama**, so the prompts and responses do not need to be sent to a cloud LLM API.
