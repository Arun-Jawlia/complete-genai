# What is Text To Math Problem
- It is AI Powered Matha nd reasoning assistant built with OpenAI, LangChain and Wikipedia.
- It can solve mathematical expressions, work through reasoning problem and search wikipedia for general knowledge


## Why agents are useful for math reasoning
- it helps in limitations of LLM because it struggle with complex calculations and hallucinations.
- It checks data from internet to provide to answer



## Difference between normal LLM response vs Agent Based reasoning
- the main difference is that a normal LLM provide a single step, passive text generation based on prompt, whereas agent based reasoning is an autonomous, multi step used as a reasoning engine to plan, use tools ad execute actions.


## Project Structure
```
GenAI-Assignment-35-Arun-Jawlia/
│
├── app.py
├── requirements.txt
└── README.md
```

## How To Run
1. Unzip the folder
2. Checkout to folder: `GenAI-Assignment-35-Arun-Jawlia`
3. install all packages: `pip install -r requirements.txt`
4. add your huggingface token in `.env` file in root 
5. Run the project `python app.py`
6. Open the local URL in your browser: ` http://localhost:8501`