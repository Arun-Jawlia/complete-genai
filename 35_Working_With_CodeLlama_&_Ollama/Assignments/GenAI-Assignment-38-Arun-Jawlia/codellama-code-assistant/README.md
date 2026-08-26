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
* CodeLlama:latest
* Streamlit

## Project Structure

```text
CodeLlama_Assignment/
│
├── app.py
├── assistant.py
├── prompts_helper.py
├── verify_ollama_model.py
├── test.py
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
CodeLlama Latest
    ↓
Generated Response
    ↓
Streamlit UI
```

# How To Run
1. First Install Ollama on your system 
2. Pull Codellama using `ollama pull codellama:latest`
3. Unzip the folder
4. Checkout to folder: `GenAI-Assignment-38-Arun-Jawlia/codellama-code-assistant`
5. Run the project `streamlit run app.py`
6. Open the local URL in your browser: ` http://localhost:8501`