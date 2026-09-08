import streamlit as st
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langsmith import traceable


load_dotenv()

st.title("Llama 3 Chatbot")

input_text = st.text_input("Enter your Question: ")

@traceable(
    name="Ollama Chatbot",
    project_name="ollama-chatbot"
)
def get_response(text):
    model = ChatOllama(model='llama3.2:1b', temperature=0)
    res = model.invoke(text)
    return res


if input_text:
    response = get_response(input_text)
    st.write(response.content)