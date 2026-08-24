# pylint: disable=all

import re
import streamlit as st

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_classic.chains import LLMChain, LLMMathChain
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.agents import Tool, initialize_agent
from langchain_classic.callbacks import StreamlitCallbackHandler

load_dotenv()

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MathMind AI",
    page_icon="🧮",
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
        background: #0b0f19;
        color: #f8fafc;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }

    /* ---------- Sidebar ---------- */

    [data-testid="stSidebar"] {
        background: #111827;
        border-right: 1px solid #1f2937;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 2rem;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 2rem;
    }

    .brand-icon {
        width: 44px;
        height: 44px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(
            135deg,
            #6366f1,
            #8b5cf6
        );
        font-size: 23px;
    }

    .brand-title {
        font-size: 20px;
        font-weight: 700;
        color: white;
        line-height: 1;
    }

    .brand-subtitle {
        color: #94a3b8;
        font-size: 12px;
        margin-top: 5px;
    }

    .sidebar-section {
        color: #64748b;
        text-transform: uppercase;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.08em;
        margin-top: 1.5rem;
        margin-bottom: 0.6rem;
    }

    .feature {
        background: #172033;
        border: 1px solid #243047;
        padding: 11px 12px;
        border-radius: 10px;
        margin-bottom: 8px;
        color: #cbd5e1;
        font-size: 13px;
    }

    .feature span {
        margin-right: 8px;
    }

    .footer {
        position: fixed;
        bottom: 15px;
        left: 20px;
        color: #64748b;
        font-size: 11px;
    }

    /* ---------- Header ---------- */

    .hero {
        text-align: center;
        padding: 20px 0 25px 0;
    }

    .hero-icon {
        font-size: 42px;
        margin-bottom: 8px;
    }

    .hero h1 {
        font-size: 38px;
        font-weight: 800;
        margin: 0;
        background: linear-gradient(
            90deg,
            #818cf8,
            #c084fc,
            #38bdf8
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        color: #94a3b8;
        font-size: 15px;
        margin-top: 10px;
    }

    /* ---------- API Key Card ---------- */

    .api-card {
        background: linear-gradient(
            135deg,
            #111827,
            #151c2d
        );
        border: 1px solid #26334b;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 25px;
    }

    /* ---------- Chat ---------- */

    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 12px;
        margin-bottom: 12px;
    }

    /* ---------- Chat Input ---------- */

    [data-testid="stChatInput"] {
        padding-bottom: 20px;
    }

    textarea {
        border-radius: 14px !important;
    }

    /* ---------- Buttons ---------- */

    .stButton > button {
        border-radius: 10px;
        border: 1px solid #334155;
        background: #1e293b;
        color: white;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        border-color: #6366f1;
        background: #26324a;
    }

    /* ---------- Suggestion Cards ---------- */

    .suggestion {
        background: #111827;
        border: 1px solid #1f2937;
        border-radius: 14px;
        padding: 15px;
        height: 100%;
        transition: all 0.2s ease;
    }

    .suggestion:hover {
        border-color: #6366f1;
        transform: translateY(-2px);
    }

    .suggestion-icon {
        font-size: 22px;
        margin-bottom: 7px;
    }

    .suggestion-title {
        color: #f8fafc;
        font-weight: 600;
        font-size: 14px;
    }

    .suggestion-text {
        color: #64748b;
        font-size: 12px;
        margin-top: 4px;
    }

    /* ---------- Hide Streamlit clutter ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="brand">
            <div class="brand-icon">🧮</div>
            <div>
                <div class="brand-title">MathMind AI</div>
                <div class="brand-subtitle">Math & Reasoning Assistant</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-section">AI Capabilities</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="feature"><span>🧮</span> Mathematical calculations</div>
        <div class="feature"><span>🧠</span> Logical reasoning</div>
        <div class="feature"><span>📚</span> Wikipedia research</div>
        <div class="feature"><span>🤖</span> AI-powered explanations</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="sidebar-section">Configuration</div>',
        unsafe_allow_html=True,
    )

    open_ai_key = st.text_input(
        "OpenAI API Key",
        type="password",
        placeholder="sk-••••••••••••••••",
        help="Your key is used only for this session.",
    )

    model_name = st.selectbox(
        "AI Model",
        ["gpt-4o", "gpt-3.5-turbo"],
        index=0,
    )

    st.divider()

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "👋 Hi! I'm **MathMind AI**. "
                    "Ask me a math, reasoning, or research question."
                ),
            }
        ]
        st.rerun()

    st.markdown(
        """
        <div class="footer">
            Powered by OpenAI + LangChain
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-icon">🧮</div>
        <h1>MathMind AI</h1>
        <p>
            Solve math problems, reason through complex questions,
            and explore knowledge with AI.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# API KEY VALIDATION
# ============================================================

if not open_ai_key:

    st.markdown(
        """
        <div class="api-card">
            <h3>🔐 Connect your OpenAI account</h3>
            <p style="color:#94a3b8;">
                Enter your OpenAI API key in the sidebar to start
                solving problems with MathMind AI.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.stop()

# ============================================================
# MODEL
# ============================================================

model = ChatOpenAI(
    model=model_name,
    api_key=open_ai_key,
)

# ============================================================
# TOOLS
# ============================================================

wikipedia_wrapper = WikipediaAPIWrapper()

wikipedia_tool = Tool(
    name="wikipedia",
    func=wikipedia_wrapper.run,
    description=(
        "Search Wikipedia for factual information and "
        "general knowledge."
    ),
)

math_chain = LLMMathChain.from_llm(llm=model)


def math_tool_func(question):
    math_expr = "".join(
        re.findall(
            r"[\d\.\+\-\*\/\^\(\)]+",
            question,
        )
    )

    if not math_expr:
        return "I couldn't identify a mathematical expression."

    return math_chain.run(math_expr)


calculator = Tool(
    name="calculator",
    func=math_tool_func,
    description=(
        "Useful for solving mathematical calculations. "
        "Input should contain a mathematical expression."
    ),
)

# ============================================================
# REASONING TOOL
# ============================================================

prompt = """
You are an expert mathematical reasoning assistant.

Solve the user's problem carefully.

Rules:
- Break the solution into clear steps.
- Explain the reasoning.
- Show important calculations.
- Give the final answer clearly.

Question:
{question}

Answer:
"""

prompt_template = PromptTemplate(
    template=prompt,
    input_variables=["question"],
)

chain = LLMChain(
    prompt=prompt_template,
    llm=model,
)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func=chain.run,
    description=(
        "Use this tool for logic, reasoning, word problems, "
        "and problems requiring a step-by-step explanation."
    ),
)

# ============================================================
# AGENT
# ============================================================

assistant_agent = initialize_agent(
    tools=[
        wikipedia_tool,
        calculator,
        reasoning_tool,
    ],
    llm=model,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True,
)

# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "👋 Hi! I'm **MathMind AI**.\n\n"
                "I can help with:\n"
                "- 🧮 Math problems\n"
                "- 🧠 Logical reasoning\n"
                "- 📚 Knowledge questions\n"
                "- 🔍 Research"
            ),
        }
    ]

# ============================================================
# CHAT HISTORY
# ============================================================

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"],
        avatar="🧮" if msg["role"] == "assistant" else "👤",
    ):
        st.markdown(msg["content"])

# ============================================================
# SUGGESTIONS
# ============================================================

if len(st.session_state.messages) == 1:

    st.markdown("### ✨ Try asking")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="suggestion">
                <div class="suggestion-icon">📐</div>
                <div class="suggestion-title">
                    Algebra
                </div>
                <div class="suggestion-text">
                    Solve 2x + 5 = 17
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="suggestion">
                <div class="suggestion-icon">🧠</div>
                <div class="suggestion-title">
                    Reasoning
                </div>
                <div class="suggestion-text">
                    Solve a logical puzzle
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="suggestion">
                <div class="suggestion-icon">📚</div>
                <div class="suggestion-title">
                    Knowledge
                </div>
                <div class="suggestion-text">
                    Ask me something about history
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask MathMind AI anything...",
)

if question:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message(
        "user",
        avatar="👤",
    ):
        st.markdown(question)

    # Generate answer
    with st.chat_message(
        "assistant",
        avatar="🧮",
    ):

        with st.spinner("Thinking..."):

            try:

                # Only use calculator when the question
                # actually looks like a direct calculation.
                math_pattern = re.fullmatch(
                    r"[\s\d\.\+\-\*\/\^\(\)]+",
                    question.strip(),
                )

                if math_pattern:

                    response = calculator.run(question)

                else:

                    st_cb = StreamlitCallbackHandler(
                        st.container(),
                        expand_new_thoughts=False,
                    )

                    response = assistant_agent.run(
                        question,
                        callbacks=[st_cb],
                    )

            except Exception as exc:

                response = (
                    "⚠️ I ran into a problem while processing "
                    f"your question.\n\n`{str(exc)}`"
                )

            st.markdown(response)

    # Save response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )
