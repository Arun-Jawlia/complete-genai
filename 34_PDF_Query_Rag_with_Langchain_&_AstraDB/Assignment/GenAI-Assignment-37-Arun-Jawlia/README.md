# PDF Query RAG using AstraDB

## Overview

This project implements a PDF Question Answering
RAG application using:

- Python
- Streamlit
- LangChain
- AstraDB
- OpenAI Embeddings
- OpenAI LLM

## Images

1. Homepage 
   ![Home](assets/database_connected.png)
2. Database 
   ![Database](assets/database.png)
3. Pdf Processed 
   ![Pdf Processed](assets/pdf_processed.png)
4. Searching in Vector Store 
   ![Searching](assets/searching.png)
5. Result 
   ![Result](assets/result.png)

## Architecture

PDF
↓
PDF Loader
↓
Text Splitter
↓
Embeddings
↓
AstraDB
↓
Retriever
↓
LLM
↓
Answer

## Features

- Upload PDF
- Split PDF into chunks
- Generate embeddings
- Store embeddings in AstraDB
- Retrieve relevant PDF chunks
- Generate grounded answers
- Handle out-of-context questions
- Streamlit session state

## How To Run
1. Unzip the folder
2. Checkout to folder: `GenAI-Assignment-37-Arun-Jawlia`
3. install all packages: `pip install -r requirements.txt`
4. Run the project `streamlit run app.py`
5. Open the local URL in your browser: ` http://localhost:8501`