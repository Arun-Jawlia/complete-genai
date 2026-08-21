# ReAct Agent

**ReAct** stands for **Reason + Act**. It is an agent pattern where an LLM doesn't just generate a final answer—it **reasons about what it needs to do, takes an action using a tool, observes the result, and continues until it can answer**.

ReAct is a Design Pattern used in AI Agent.

The core loop is:

> **Reason → Act → Observe → Reason → Act → Observe → Final Answer**

This is one of the foundational patterns for building **AI Agents**.

---

## 1. Why do we need ReAct?

A normal LLM works roughly like:

```text
User Question
     ↓
     LLM
     ↓
Final Answer
```

Suppose you ask:

> "What is the current weather in Delhi and should I carry an umbrella?"

A normal LLM may know general weather information, but it doesn't automatically have access to the **current weather**.

An agent can use a weather tool:

```text
User
 ↓
LLM
 ↓
"Need current weather"
 ↓
Weather Tool
 ↓
Weather Result
 ↓
LLM
 ↓
"Rain is expected → carry umbrella"
```

The agent is therefore able to **interact with the outside world**.

---

# 2. What does ReAct mean?

ReAct combines:

### Reasoning

The model determines:

> "What do I need to figure out?"

### Acting

The model decides:

> "Which tool should I use?"

### Observation

The model receives:

> "What did the tool return?"

Then it reasons again.

```text
                 ┌───────────────┐
                 │     User      │
                 └───────┬───────┘
                         ↓
                 ┌───────────────┐
                 │      LLM      │
                 └───────┬───────┘
                         ↓
                    Reasoning
                         ↓
                    Choose Tool
                         ↓
                 ┌───────────────┐
                 │     Tool      │
                 └───────┬───────┘
                         ↓
                    Observation
                         ↓
                 ┌───────────────┐
                 │      LLM      │
                 └───────┬───────┘
                         ↓
                    More reasoning
                         ↓
                    Final Answer
```

---

# 3. Simple Example

Suppose the user asks:

> "What is the population of India, and calculate what 5% of it is."

The agent might perform:

### Step 1 — Reason

```text
I need the current population of India.
```

### Step 2 — Act

```text
Call population/search tool
```

### Step 3 — Observe

```text
Population = X
```

### Step 4 — Reason

```text
Now calculate 5% of X.
```

### Step 5 — Act

```text
Call calculator
```

### Step 6 — Observe

```text
5% of X = Y
```

### Step 7 — Final Answer

```text
India's population is approximately X.
5% of that is approximately Y.
```

The important point is that **the LLM dynamically decides what action to take based on the current situation**.

---

# 4. ReAct vs Normal LLM

| Normal LLM                 | ReAct Agent                                |
| -------------------------- | ------------------------------------------ |
| Generates answer           | Reasons + acts                             |
| Usually one-shot           | Iterative                                  |
| No tools by default        | Can use tools                              |
| Static knowledge           | Can obtain external information            |
| No environment interaction | Can interact with environment              |
| Question → Answer          | Question → Reason → Act → Observe → Answer |

---

# 5. ReAct Components

A ReAct agent typically contains:

### 1. LLM

The brain of the agent.

Examples:

* GPT
* Claude
* Gemini
* Llama
* Mistral

---

### 2. Tools

Tools allow the agent to interact with external systems.

Examples:

```text
Search Tool
Calculator
Weather API
Database
Python
Code Executor
File Reader
Browser
Email
CRM
```

---

### 3. Prompt

The prompt tells the LLM:

* what its role is
* what tools are available
* when to use them
* what information to provide to tools

---

### 4. Agent Loop

The loop manages:

```text
LLM
 ↓
Tool Call
 ↓
Tool Result
 ↓
LLM
 ↓
Tool Call
 ↓
Tool Result
 ↓
Final Answer
```

---

### 5. Memory / State

The agent needs to maintain the information collected during execution.

For example:

```text
User Question
     ↓
Search Result
     ↓
Calculation Result
     ↓
Database Result
     ↓
Final Answer
```

---

# 6. ReAct in LangChain

Since you're learning LangChain, this is especially important.

Conceptually:

```python
from langchain.agents import create_agent
```

You provide:

```text
LLM
+
Tools
+
Instructions
```

For example:

```python
tools = [
    calculator_tool,
    search_tool
]

agent = create_agent(
    model,
    tools=tools,
    system_prompt="You are a helpful assistant."
)
```

Then:

```python
response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is 25% of India's population?"
        }
    ]
})
```

The agent can decide:

```text
User Question
      ↓
     LLM
      ↓
Need population
      ↓
Search Tool
      ↓
Population
      ↓
Calculate 25%
      ↓
Calculator Tool
      ↓
Result
      ↓
Final Answer
```

The exact LangChain APIs evolve, so when implementing this in a current project, use the version-specific agent API rather than older `initialize_agent` examples.

---

# 7. ReAct Prompt

Historically, ReAct was often represented with a structured interaction such as:

```text
Question
Thought
Action
Action Input
Observation
Thought
Action
Action Input
Observation
Final Answer
```

For example:

```text
Question:
What is 20% of the current population of India?

Thought:
I need the current population first.

Action:
Search

Action Input:
current population of India

Observation:
Population ≈ X

Thought:
Now I need to calculate 20% of X.

Action:
Calculator

Action Input:
X * 0.20

Observation:
Y

Final Answer:
20% of India's population is approximately Y.
```

This is the classic **ReAct pattern**.

Modern agent frameworks often implement this loop internally rather than exposing raw `Thought` text.

---

# 8. ReAct is NOT just Chain-of-Thought

This distinction is important.

### Chain-of-Thought

The model reasons internally:

```text
Question
 ↓
Reason
 ↓
Answer
```

### ReAct

The model reasons about **what action to take**:

```text
Question
 ↓
Reason
 ↓
Tool
 ↓
Observation
 ↓
Reason
 ↓
Tool
 ↓
Observation
 ↓
Answer
```

So:

> **Chain-of-Thought = reasoning**

while:

> **ReAct = reasoning + interaction/action**

---

# 9. ReAct vs Chain

A normal LangChain chain might be:

```text
Input
 ↓
Prompt
 ↓
LLM
 ↓
Output Parser
 ↓
Output
```

The path is predetermined.

For example:

```text
Question
 ↓
Retriever
 ↓
LLM
 ↓
Answer
```

A ReAct agent is more dynamic:

```text
Question
 ↓
LLM
 ↓
Should I search?
 ├── Yes → Search
 │          ↓
 │       Observation
 │          ↓
 └──────── LLM
            ↓
       Should I calculate?
         ├── Yes → Calculator
         │          ↓
         │       Observation
         ↓
      Final Answer
```

The **LLM chooses the next step**.

---

# 10. ReAct vs RAG

These are often confused.

### RAG

RAG is primarily:

```text
Question
 ↓
Retrieve relevant documents
 ↓
LLM
 ↓
Answer
```

Example:

> "What does our company's leave policy say?"

The system retrieves the relevant document and gives it to the LLM.

---

### ReAct Agent

A ReAct agent can decide:

```text
Question
 ↓
LLM
 ↓
Search?
 ↓
Database?
 ↓
Calculator?
 ↓
Python?
 ↓
Another tool?
 ↓
Final Answer
```

So RAG can actually be **one tool available to a ReAct agent**.

For example:

```text
                ReAct Agent
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    Search        RAG       Calculator
       ↓            ↓            ↓
    Web data    Documents    Calculations
```

---

# 11. Real-World Example

Imagine you're building an **AI Software Engineering Agent**.

The user asks:

> "Why is my application returning a 500 error?"

The ReAct agent could have:

```text
Tools:

GitHub Tool
↓
Read repository

File Tool
↓
Read source code

Terminal Tool
↓
Run commands

Database Tool
↓
Inspect database

Search Tool
↓
Search documentation

Test Tool
↓
Run tests
```

The agent might execute:

```text
User
 ↓
LLM
 ↓
Read error logs
 ↓
GitHub Tool
 ↓
Find controller
 ↓
LLM
 ↓
Inspect database schema
 ↓
Database Tool
 ↓
Find mismatch
 ↓
LLM
 ↓
Modify code
 ↓
Terminal Tool
 ↓
Run tests
 ↓
Tests pass
 ↓
Final Answer
```

That's a much more powerful system than simply asking an LLM:

> "Fix my 500 error."

---

# 12. Advantages

### ✅ Dynamic decision making

The agent chooses tools based on the problem.

### ✅ Tool usage

It can interact with:

* APIs
* databases
* files
* browsers
* code execution environments

### ✅ Multi-step problem solving

It can perform several actions sequentially.

### ✅ Adaptability

If one tool returns unexpected information, the agent can change its next action.

### ✅ Useful for autonomous systems

For example:

```text
Research Agent
Coding Agent
Customer Support Agent
Data Analyst Agent
Travel Agent
DevOps Agent
Resume Agent
```

---

# 13. Limitations

ReAct isn't magic.

### ❌ More expensive

Every reasoning/tool iteration can require additional model calls.

### ❌ Slower

Multiple tool calls mean increased latency.

### ❌ Tool errors

A bad API response can cause the agent to make a bad decision.

### ❌ Infinite loops

Poorly designed agents can repeatedly call tools.

### ❌ Hallucination

The model can still misunderstand tool results.

### ❌ Security risks

Giving an agent powerful tools like:

```text
shell
database
file deletion
production deployment
```

requires strict permissions and safeguards.

---

# 14. ReAct Agent Architecture

A production architecture can look like:

```text
                    ┌──────────────┐
                    │     User     │
                    └──────┬───────┘
                           ↓
                    ┌──────────────┐
                    │  Agent LLM   │
                    └──────┬───────┘
                           ↓
                 ┌────────────────────┐
                 │   Agent Decision   │
                 └─────────┬──────────┘
                           ↓
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
   Search Tool        Database Tool       Python Tool
        ↓                  ↓                  ↓
        └──────────────────┼──────────────────┘
                           ↓
                      Observation
                           ↓
                      Agent LLM
                           ↓
                    Need another tool?
                      /          \
                    Yes           No
                    ↓              ↓
                 Tool Call     Final Answer
                    ↓
                Observation
                    ↓
                   LLM
```

---

# 15. The most important concept

When learning agents, remember this:

```text
LLM
+
Tools
+
Decision Making
+
Loop
=
Agent
```

And the classic ReAct loop is:

```text
             ┌───────────────┐
             │     REASON    │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │      ACT      │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │   OBSERVE     │
             └───────┬───────┘
                     ↓
                  REASON
                     ↓
                   ACT
                     ↓
                 OBSERVE
                     ↓
                  FINISH
```

### In one sentence:

> **A ReAct Agent is an LLM-based agent that repeatedly decides what to do, calls an appropriate tool, observes the result, and uses that result to decide its next step until it can produce the final answer.**

For your **GenAI/LangChain learning path**, the natural progression after ReAct is:

**Tools → Tool Calling → ReAct → Agent Executor/Agent Loop → Memory/State → RAG Agent → LangGraph → Multi-Agent Systems.**


---
Tool Calling is related to ReAct Agent

Tool Execution is part of Agent Executor

Tool Calling: Thought + Action + Action Input


Agnet and Agent Executor
1. Agent exector orchestrates the Entire loop
2. Send inputs and previous messages to the agent
3. Get the next action from agent
4. Executes the tool with the provided inputs
5. Add the tool's observation back into the history
6. Finally, Loops again with the updated hisotry untill the agent says the final answer