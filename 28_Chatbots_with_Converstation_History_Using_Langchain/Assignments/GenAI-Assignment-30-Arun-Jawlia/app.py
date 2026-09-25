import os
import streamlit as st

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

st.title("🤖 Groq RAG Chatbot")

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = st.text_input(
        "Enter Groq API Key",
        type="password"
    )

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

if "messages" not in st.session_state:
    st.session_state.messages = []


if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

uploaded_file = st.file_uploader("Upload PDF or TXT",type=["pdf", "txt"])

if uploaded_file is not None:

    file_path = uploaded_file.name

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    if uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    st.session_state.vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    st.success("Document processed successfully!")


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


question = st.chat_input(
    "Ask a question about your document..."
)


if question:

    if st.session_state.vectorstore is None:

        st.warning("Please upload a document first.")

    else:
        with st.chat_message("user"):
            st.write(question)

        chat_history = []

        for message in st.session_state.messages:
            if message["role"] == "user":
                chat_history.append(HumanMessage(content=message["content"]))
            elif message["role"] == "assistant":
                chat_history.append(AIMessage(content=message["content"]))

        retriever = st.session_state.vectorstore.as_retriever(
            search_kwargs={"k": 3}
        )

        retrieved_docs = retriever.invoke(question)
        context = "\n\n".join(
            doc.page_content
            for doc in retrieved_docs
        )

        rag_prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """You are a document Q&A assistant.

        Answer the user's question ONLY using the provided context.

        Use the conversation history to understand follow-up questions.

        If the answer is not available in the context, say:
        "I don't know."

        Do not use outside knowledge.

        Context:
        {context}
        """
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}")
        ])

        # Create prompt
        messages = rag_prompt.invoke({
            "context": context,
            "chat_history": chat_history,
            "question": question
        })

        response = llm.invoke(messages)

        answer = response.content
        with st.chat_message("assistant"):
            st.write(answer)
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })