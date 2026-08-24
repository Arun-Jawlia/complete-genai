#pylint: disable = all

import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_classic.chains import LLMChain, LLMMathChain
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents.agent_types import AgentType
from langchain_classic.agents import Tool, initialize_agent
from langchain_classic.callbacks import StreamlitCallbackHandler
import re

load_dotenv()

st.title("Text To Math Problem Solver using OpenAI gpt-4o")
st.write('App Math + Reasoning chatbot')

default_openai_model = 'gpt-4o'

open_ai_key = st.sidebar.text_input("Please enter your OpenAI Api key", type='password')

if not open_ai_key:
    st.info("Please enter your Openai Api key")
    st.stop()

model = ChatOpenAI(model=default_openai_model)

# Initialize Agents
wikipedia_wrapper = WikipediaAPIWrapper()

wikipedia_tool = Tool(
    name='wikipedia',
    func = wikipedia_wrapper.run,
    description='Agent used for searching over the internet to find various information'
)

math_chain = LLMMathChain.from_llm(llm=model)

def math_tool_func(question):
    math_expr=  "".join(re.findall(r'[\d\.\+\-\*\/\^\(\)]+', question))
    return math_chain.run(math_expr)

calculator = Tool(
    name='calculator',
    func = math_tool_func,
    description='Tool usef for answering math related question. Only input mathematical '
)

prompt = '''
    You are an agent Tasked with solving user mathematical problem.
    Logically arriave at the solution and display it point wise for the question below:
    Question: {question}
    Answer:
'''

prompt_template = PromptTemplate(template=prompt, input_variables=['question'])

chain = LLMChain(prompt=prompt_template, llm = model)

Reasoning = Tool(
    name = "Reasoning Tool",
    func = chain.run,
    description = 'A Tool used for answering logic based and reasoning questions'
)

# Build the agent

assistant_agent = initialize_agent(
    tools = [wikipedia_tool, calculator, Reasoning],
    llm = model,
    AgentType = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = False,
    handle_parsing_errors = True
)

if 'messages' not in st.session_state:
    st.session_state['messages'] = [{'role':"assistant", 'content':"🤖 Hi I am Math Chatbot who can answer all your Maths Questions"}]


for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

question = st.text_area("Please Ask your question")

if st.button('Find my Answer'):
    if question:
        with st.spinner("Generating Response..."):
            st.session_state.messages.append({
                'role':'user',
                'content':question
            })
            st.chat_message('user').write(question)

        if re.search(r'[\d\.\+\-\*\/\^\(\)]+', question):
            response = calculator.run(question)
        else:
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = assistant_agent.run(question, callbacks=[st_cb])

        st.session_state.messages.append({
            'role':'assistant',
            "content":response
        })
        st.chat_message('assistant').write(response)
    else:
        st.write("Please ask your question")