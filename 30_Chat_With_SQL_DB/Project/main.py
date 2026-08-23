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


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SQL Speak",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- Global ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(99, 102, 241, 0.10),
                transparent 28%
            ),
            radial-gradient(
                circle at 85% 20%,
                rgba(14, 165, 233, 0.08),
                transparent 25%
            ),
            #0b1120;
    }

    .main .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #0f172a 0%,
            #111827 100%
        );
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.5rem;
    }

    /* ---------- Header ---------- */

    .app-header {
        padding: 1.5rem 0 1rem 0;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 14px;
    }

    .brand-icon {
        width: 52px;
        height: 52px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 27px;
        background: linear-gradient(
            135deg,
            #6366f1,
            #06b6d4
        );
        box-shadow: 0 10px 30px rgba(99,102,241,.25);
    }

    .brand-title {
        font-size: 2.1rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        color: #f8fafc;
        margin: 0;
    }

    .brand-subtitle {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-top: 2px;
    }

    /* ---------- Status Cards ---------- */

    .status-card {
        background: rgba(15, 23, 42, 0.72);
        border: 1px solid rgba(148,163,184,0.12);
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 12px;
        backdrop-filter: blur(12px);
    }

    .status-label {
        color: #94a3b8;
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: .08em;
        font-weight: 700;
    }

    .status-value {
        color: #f8fafc;
        font-size: 1rem;
        font-weight: 600;
        margin-top: 4px;
    }

    .online {
        color: #34d399;
    }

    /* ---------- Welcome ---------- */

    .welcome-card {
        text-align: center;
        padding: 3.5rem 2rem;
        margin: 3rem auto 2rem;
        max-width: 760px;
        border-radius: 24px;
        background:
            linear-gradient(
                145deg,
                rgba(30,41,59,.78),
                rgba(15,23,42,.72)
            );
        border: 1px solid rgba(148,163,184,.12);
        box-shadow: 0 25px 70px rgba(0,0,0,.25);
    }

    .welcome-icon {
        font-size: 3.5rem;
        margin-bottom: 1rem;
    }

    .welcome-title {
        color: #f8fafc;
        font-size: 1.8rem;
        font-weight: 750;
        margin-bottom: .6rem;
    }

    .welcome-text {
        color: #94a3b8;
        max-width: 560px;
        margin: auto;
        line-height: 1.7;
    }

    /* ---------- Suggestion Cards ---------- */

    .suggestion {
        background: rgba(30,41,59,.55);
        border: 1px solid rgba(148,163,184,.10);
        border-radius: 12px;
        padding: 12px 14px;
        color: #cbd5e1;
        font-size: .88rem;
        height: 100%;
    }

    .suggestion strong {
        color: #f8fafc;
    }

    /* ---------- Chat ---------- */

    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.75rem;
    }

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-user"]
    ) {
        background: rgba(30,41,59,.35);
    }

    [data-testid="stChatMessage"]:has(
        [data-testid="chatAvatarIcon-assistant"]
    ) {
        background: rgba(15,23,42,.45);
        border: 1px solid rgba(99,102,241,.08);
    }

    /* ---------- Input ---------- */

    [data-testid="stChatInput"] {
        border-radius: 18px;
    }

    [data-testid="stChatInput"] textarea {
        border-radius: 16px;
    }

    /* ---------- Buttons ---------- */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid rgba(148,163,184,.15);
        transition: all .2s ease;
    }

    .stButton > button:hover {
        border-color: rgba(99,102,241,.5);
        transform: translateY(-1px);
    }

    /* ---------- Divider ---------- */

    .soft-divider {
        height: 1px;
        background: rgba(148,163,184,.10);
        margin: 1rem 0;
    }

    /* ---------- Hide Streamlit branding ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

LOCALDB = "USE_LOCALDB"
MYSQLDB = "USE_MYSQL"

DEFAULT_OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o",
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🗄️</div>
            <div>
                <div style="
                    color:#f8fafc;
                    font-size:1.35rem;
                    font-weight:800;
                ">
                    SQL Speak
                </div>
                <div style="
                    color:#64748b;
                    font-size:.78rem;
                ">
                    AI Database Assistant
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

    st.markdown("### ⚙️ Configuration")

    radio_options = [
        "Use SQLite3 Database",
        "Connect to MySQL",
    ]

    selected_option = st.radio(
        "Database",
        options=radio_options,
        index=0,
        label_visibility="collapsed",
    )

    if selected_option == "Connect to MySQL":

        db_url = MYSQLDB

        st.markdown("#### MySQL Connection")

        mysql_host = st.text_input(
            "Hostname",
            value="localhost",
            placeholder="localhost",
        )

        mysql_user = st.text_input(
            "Username",
            value="root",
        )

        mysql_password = st.text_input(
            "Password",
            type="password",
        )

        mysql_db = st.text_input(
            "Database name",
            placeholder="my_database",
        )

    else:

        db_url = LOCALDB

        st.markdown(
            """
            <div class="status-card">
                <div class="status-label">Local database</div>
                <div class="status-value">📁 student.db</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### 🤖 AI Model")

    openai_api = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="sk-••••••••••••",
    )

    openai_model_name = st.text_input(
        "Model",
        value=DEFAULT_OPENAI_MODEL,
    )

    st.markdown('<div class="soft-divider"></div>', unsafe_allow_html=True)

    if st.button(
        "🗑️ Clear conversation",
        use_container_width=True,
    ):
        st.session_state["messages"] = [
            {
                "role": "assistant",
                "content": (
                    "👋 Conversation cleared. "
                    "What would you like to know about your database?"
                ),
            }
        ]
        st.rerun()

    st.markdown(
        """
        <div style="
            position: fixed;
            bottom: 20px;
            color:#475569;
            font-size:.72rem;
        ">
            SQL Speak · AI-powered database exploration
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# API KEY
# ============================================================

if not openai_api:
    st.markdown(
        """
        <div class="welcome-card">
            <div class="welcome-icon">🔐</div>
            <div class="welcome-title">
                Connect your AI assistant
            </div>
            <div class="welcome-text">
                Enter your OpenAI API key in the sidebar to start
                asking natural-language questions about your database.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.stop()


# ============================================================
# OPENAI
# ============================================================

openai_model = ChatOpenAI(
    model=openai_model_name,
    api_key=openai_api,
    streaming=True,
)


# ============================================================
# DATABASE
# ============================================================

@st.cache_resource(ttl=7200)
def configure_db(
    db_url,
    mysql_host=None,
    mysql_user=None,
    mysql_password=None,
    mysql_db=None,
):

    if db_url == LOCALDB:

        dbfilepath = (
            Path(__file__).parent / "student.db"
        ).absolute()

        if not dbfilepath.exists():
            st.error(
                f"SQLite database not found: {dbfilepath}"
            )
            st.stop()

        creator = lambda: sqlite3.connect(
            f"file:{dbfilepath}?mode=ro",
            uri=True,
            check_same_thread=False,
        )

        return SQLDatabase(
            create_engine(
                "sqlite://",
                creator=creator,
            )
        )

    if db_url == MYSQLDB:

        if not (
            mysql_host
            and mysql_user
            and mysql_password
            and mysql_db
        ):
            st.error(
                "Please provide all MySQL connection details."
            )
            st.stop()

        encoded_password = quote_plus(
            mysql_password
        )

        connection_str = (
            f"mysql+mysqlconnector://"
            f"{mysql_user}:{encoded_password}"
            f"@{mysql_host}/{mysql_db}"
        )

        try:
            return SQLDatabase(
                create_engine(connection_str)
            )

        except Exception as e:
            st.error(
                f"Failed to connect to MySQL: {e}"
            )
            st.stop()

    st.error("Invalid database option selected.")
    st.stop()


if db_url == MYSQLDB:

    db = configure_db(
        db_url,
        mysql_host,
        mysql_user,
        mysql_password,
        mysql_db,
    )

else:

    db = configure_db(db_url)


# ============================================================
# AGENT
# ============================================================

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=openai_model,
)

agent = create_sql_agent(
    llm=openai_model,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
)


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    """
    <div class="app-header">
        <div class="brand">
            <div class="brand-icon">💬</div>
            <div>
                <div class="brand-title">
                    SQL Speak
                </div>
                <div class="brand-subtitle">
                    Talk to your database in plain English
                </div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# STATUS ROW
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    db_name = (
        "SQLite · student.db"
        if db_url == LOCALDB
        else f"MySQL · {mysql_db}"
    )

    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-label">Database</div>
            <div class="status-value">
                🟢 {db_name}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        f"""
        <div class="status-card">
            <div class="status-label">AI Model</div>
            <div class="status-value">
                ✨ {openai_model_name}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="status-card">
            <div class="status-label">Status</div>
            <div class="status-value online">
                ● Connected
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": (
                "👋 Hi! I'm SQL Speak.\n\n"
                "Ask me anything about your database "
                "using natural language."
            ),
        }
    ]


for msg in st.session_state["messages"]:

    avatar = (
        "🧑‍💻"
        if msg["role"] == "user"
        else "🤖"
    )

    with st.chat_message(
        msg["role"],
        avatar=avatar,
    ):
        st.markdown(msg["content"])


# ============================================================
# WELCOME SUGGESTIONS
# ============================================================

# if len(st.session_state["messages"]) == 1:

#     st.markdown(
#         """
#         <div class="welcome-card">
#             <div class="welcome-icon">🧠</div>

#             <div class="welcome-title">
#                 Ask your database anything
#             </div>

#             <div class="welcome-text">
#                 SQL Speak converts your questions into SQL,
#                 executes the query, and explains the results
#                 in an easy-to-understand way.
#             </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.markdown(
#             """
#             <div class="suggestion">
#                 🔎<br>
#                 <strong>Explore data</strong><br>
#                 Show me all users
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with col2:
#         st.markdown(
#             """
#             <div class="suggestion">
#                 📊<br>
#                 <strong>Analyze data</strong><br>
#                 What are the top products?
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#     with col3:
#         st.markdown(
#             """
#             <div class="suggestion">
#                 🔗<br>
#                 <strong>Join tables</strong><br>
#                 Show users and their orders
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )


# ============================================================
# USER INPUT
# ============================================================

user_query = st.chat_input(
    placeholder="Ask a question about your database..."
)


if user_query:

    # User message
    st.session_state["messages"].append(
        {
            "role": "user",
            "content": user_query,
        }
    )

    with st.chat_message(
        "user",
        avatar="🧑‍💻",
    ):
        st.markdown(user_query)

    # Assistant
    with st.chat_message(
        "assistant",
        avatar="🤖",
    ):

        streamlit_callback = StreamlitCallbackHandler(
            st.container()
        )

        try:

            with st.spinner("Thinking..."):

                result = agent.invoke(
                    {"input": user_query},
                    config={
                        "callbacks": [
                            streamlit_callback
                        ]
                    },
                )

            response = result.get(
                "output",
                "I could not generate a response.",
            )

            st.markdown(response)

        except Exception as e:

            response = (
                "I ran into a problem while querying "
                "the database."
            )

            st.error(response)

            with st.expander(
                "Show technical details"
            ):
                st.code(
                    str(e),
                    language="text",
                )

        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": response,
            }
        )
