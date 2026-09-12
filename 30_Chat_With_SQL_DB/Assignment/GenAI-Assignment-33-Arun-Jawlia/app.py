# pylint: disable=all
import os
import sqlite3
from pathlib import Path
from urllib.parse import quote_plus

import streamlit as st
from dotenv import load_dotenv
from langchain_classic.agents import AgentType
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from langchain_openai import ChatOpenAI


load_dotenv()

st.title("SQL Speak: Chat with the Database")

LOCALDB = "USE_LOCALDB"
MYSQLDB = "USE_MYSQL"
DEFAULT_OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

radio_options = ["Use SQLite3 Database(student.db)", "Connect to MySQL Database"]
selected_option = st.sidebar.radio("Choose the DB you want to chat with", options=radio_options)

if selected_option == "Connect to MySQL Database":
    db_url = MYSQLDB
    mysql_host = st.sidebar.text_input("Provide MySQL Hostname", value="localhost")
    mysql_user = st.sidebar.text_input("Provide MySQL Username", value="root")
    mysql_password = st.sidebar.text_input("Provide MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("Provide MySQL Database Name")
else:
    db_url = LOCALDB

openai_api = st.sidebar.text_input(
    "Provide the OPENAI API Key",
    # value=os.getenv("OPENAI_API_KEY", ""),
    type="password",
)
openai_model_name = st.sidebar.text_input("OpenAI model", value=DEFAULT_OPENAI_MODEL)

if not openai_api:
    st.info("Please provide the OPENAI API Key")
    st.stop()

openai_model = ChatOpenAI(model=openai_model_name, api_key=openai_api, streaming=True)


@st.cache_resource(ttl=7200)
def configure_db(db_url, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_url == LOCALDB:
        dbfilepath = (Path(__file__).parent / "student.db").absolute()

        if not dbfilepath.exists():
            st.error(f"SQLite database not found: {dbfilepath}")
            st.stop()

        creator = lambda: sqlite3.connect(
            f"file:{dbfilepath}?mode=ro",
            uri=True,
            check_same_thread=False,
        )

        return SQLDatabase(create_engine("sqlite://", creator=creator))

    if db_url == MYSQLDB:
        if not (mysql_host and mysql_user and mysql_password and mysql_db):
            st.error("Please provide all MySQL connection details")
            st.stop()

        encoded_password = quote_plus(mysql_password)
        connection_str = (
            f"mysql+mysqlconnector://{mysql_user}:{encoded_password}@{mysql_host}/{mysql_db}"
        )

        try:
            db = SQLDatabase(create_engine(connection_str))
            st.success("Successfully connected to MySQL database")
            return db
        except Exception as e:
            st.error(f"Failed to connect to MySQL: {e}")
            st.stop()

    st.error("Invalid database option selected")
    st.stop()


if db_url == MYSQLDB:
    db = configure_db(db_url, mysql_host, mysql_user, mysql_password, mysql_db)
else:
    db = configure_db(db_url)

toolkit = SQLDatabaseToolkit(db=db, llm=openai_model)
agent = create_sql_agent(
    llm=openai_model,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

if st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you?"}
    ]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

user_query = st.chat_input(placeholder="Ask anything from the database...")

if user_query:
    st.session_state["messages"].append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        streamlit_callback = StreamlitCallbackHandler(st.container())
        try:
            result = agent.invoke(
                {"input": user_query},
                config={"callbacks": [streamlit_callback]},
            )
            response = result.get("output", "I could not generate a response.")
        except Exception as e:
            response = f"Error while getting result: {e}"
            st.error(response)

        st.session_state["messages"].append({"role": "assistant", "content": response})
        st.write(response)
