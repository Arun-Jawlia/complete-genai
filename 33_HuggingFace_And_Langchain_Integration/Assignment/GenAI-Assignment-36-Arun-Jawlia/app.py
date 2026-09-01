#pylint: disable=all

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

client = InferenceClient(
    model="meta-llama/Llama-3.1-8B-Instruct",
    token=os.getenv("HF_TOKEN")
)

prompt = 'Explain Huggingface'

response = client.chat_completion(
    messages=[{"role": "user","content": "Explain Generative AI in simple terms."}],
    max_tokens=100
)

print("response")


llm = HuggingFaceEndpoint(
    repo_id='google/flan-t5-base',
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=100
)

chat_model = ChatHuggingFace(llm = llm)

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI Teacher"),
    ("human", "{question}")
])

chain = prompt | chat_model

result = chain.invoke({
    "question": 'What is RAG?'
})

print(result.content)