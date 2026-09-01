#pylint: disable = all
import cassio
from langchain_community.vectorstores import Cassandra
from langchain_classic.indexes.vectorstore import VectorStoreIndexWrapper
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
import streamlit as st


load_dotenv()

ASTRA_DB_TOKEN = os.getenv('ASTRADB_APPLICATION_TOKEN')
ASTRA_DB_ID = os.getenv('ASTRADB_ID')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not ASTRA_DB_TOKEN:
    st.error("ASTRA_DB_TOKEN is missing.")
    st.stop()

if not ASTRA_DB_ID:
    st.error("ASTRA_DB_ID is missing.")
    st.stop()

if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY is missing.")
    st.stop()


st.set_page_config(
    page_title='PDF AstraDB RAG',
    page_icon = '',
    layout='wide'
)

st.title('PDF Question Answering RAG')

st.write(
    "Ask question about the your upload pdf",
    "Powered by Langchain + AstraDB + OpenAI"
)

if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None

if 'indexes' not in st.session_state:
    st.session_state.indexes = None

if 'processed' not in st.session_state:
    st.session_state.processed = False

def connect_to_astra_db():
    try:
        cassio.init(token = ASTRA_DB_TOKEN, database_id=ASTRA_DB_ID)
        st.success('Connected to AstraDB Successfully')
    except Exception as e:
        st.error(f"Connection Failed :{e}")
        st.stop()

def generateEmbeddings():
    embeddings = OpenAIEmbeddings(
        model='text-embedding-3-small'
    )
    return embeddings

def create_vector_store():
    try:
        if st.session_state.vector_store is None:
            st.session_state.vector_store = Cassandra(
                embedding= generateEmbeddings(),
                table_name ='pdf_rag_table',
                # session=None,
                # keyspace=None
            )
    except Exception as e:
        st.error(f'Unable to create vector store: {e}')
        st.stop()

connect_to_astra_db()
create_vector_store()

uploaded_file = st.file_uploader("Upload a PDF", type=['pdf'])

if uploaded_file is not None:

    if st.button('Process'):

        with st.spinner('in process...'):
            pdfReader = PdfReader(uploaded_file)
            
            raw_text = ""

            for page in pdfReader.pages:
                text = page.extract_text()
                if text:
                    raw_text += text + '\n'
            
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap = 200
            )
            texts = text_splitter.split_text(raw_text)


            st.session_state.vector_store.add_texts(texts)

            st.session_state.indexes = (
                VectorStoreIndexWrapper(
                    vectorstore = st.session_state.vector_store
                )
            )

            st.session_state.processed = True
            st.success(
                f"PDF processed successfully — {len(texts)} chunks stored in AstraDB."
            )


if st.session_state.processed:
    st.divider()

    st.subheader("Ask a Question")

    question = st.text_input("Enter your question")

    if st.button('Ask Question'):

        if not question.strip():
            st.warning("please enter a questions")
        else:

            try:
                with st.spinner("Searching in pdf..."):

                    llm = ChatOpenAI(model='gpt-4o', temperature=0)
                    answer = st.session_state.indexes.query(question, llm=llm)

                st.subheader('Anwser')

                st.write(answer)

            except Exception as e:
                st.error(f'Question answering failed: {e}')