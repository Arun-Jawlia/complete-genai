# Tool Calling and Tool Execution in LangChain

**Tool Calling** and **Tool Execution** are two different stages of an AI Agent workflow.

The easiest way to remember them:

> **Tool Calling = LLM decides what tool should be used and generates the arguments.**
> **Tool Execution = Your application/agent actually runs that tool.**

This distinction is fundamental for understanding LangChain Agents.

---

# 1. Big Picture

Suppose we create this tool:

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

User asks:

```text
What is 25 × 40?
```

The complete flow is:

```text
User
  ↓
LLM
  ↓
Tool Calling
  ↓
multiply(a=25, b=40)
  ↓
Tool Execution
  ↓
1000
  ↓
Tool Result
  ↓
LLM
  ↓
Final Answer
```

There are therefore **two distinct operations**:

```text
                 Tool Calling
                      ↓
             "Call multiply"
                      ↓
                 Tool Execution
                      ↓
                    1000
```

---

# 2. What Is Tool Calling?

**Tool calling** is when the LLM determines that it needs an external capability and generates a structured request to invoke that tool.

For example:

```text
User:
What is 25 × 40?

LLM:
I should use the multiply tool.

Tool Call:
multiply(
    a=25,
    b=40
)
```

The important point:

> The LLM has **requested** the tool. It has not necessarily executed it.

---

# 3. What Is Tool Execution?

Tool execution is the actual invocation of the underlying function.

If the model generates:

```text
multiply(
    a=25,
    b=40
)
```

your application executes:

```python
multiply.invoke({
    "a": 25,
    "b": 40
})
```

The result is:

```text
1000
```

That's **tool execution**.

---

# 4. The Difference

| Tool Calling                          | Tool Execution                        |
| ------------------------------------- | ------------------------------------- |
| Performed by/model-generated request  | Performed by application/tool runtime |
| Decides which tool                    | Actually runs tool                    |
| Generates arguments                   | Uses arguments                        |
| Produces `tool_calls`                 | Produces tool result                  |
| Does not necessarily execute anything | Executes real code/API/database       |
| Part of LLM response                  | Part of application execution         |

Remember:

```text
LLM → Tool Call
Application → Tool Execution
```

---

# 5. Complete Tool Calling Architecture

```text
                         USER
                           │
                           ▼
                  ┌─────────────────┐
                  │      LLM        │
                  │ + Bound Tools   │
                  └────────┬────────┘
                           │
                           │
                     Tool Calling
                           │
                           ▼
                  ┌─────────────────┐
                  │   tool_calls    │
                  │                 │
                  │ name: multiply  │
                  │ a: 25            │
                  │ b: 40            │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Tool Execution  │
                  └────────┬────────┘
                           │
                           ▼
                       multiply()
                           │
                           ▼
                         1000
                           │
                           ▼
                  ┌─────────────────┐
                  │  ToolMessage    │
                  │     1000        │
                  └────────┬────────┘
                           │
                           ▼
                         LLM
                           │
                           ▼
                    Final Answer
```

---

# 6. Step 1 — Create a Tool

Let's start with a simple custom tool.

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

Our tool contains:

```text
Name        → multiply
Description → Multiply two numbers
Input       → a, b
Output      → integer
```

---

# 7. Step 2 — Create the LLM

For example:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4.1-mini"
)
```

---

# 8. Step 3 — Bind the Tool

Now we tell the LLM:

> "This tool is available to you."

```python
llm_with_tools = llm.bind_tools([
    multiply
])
```

This is **tool binding**.

At this point:

```text
LLM
 +
Tool Definition
```

But the tool hasn't executed.

---

# 9. Step 4 — User Sends a Request

```python
response = llm_with_tools.invoke(
    "What is 25 multiplied by 40?"
)
```

The model analyzes the request.

It sees:

```text
Question:
25 × 40

Available Tool:
multiply(a, b)
```

It decides:

```text
I should call multiply.
```

---

# 10. Step 5 — Tool Calling

The model returns an `AIMessage` containing a tool call.

Conceptually:

```python
response.tool_calls
```

might contain:

```python
[
    {
        "name": "multiply",
        "args": {
            "a": 25,
            "b": 40
        },
        "id": "call_123"
    }
]
```

This is **Tool Calling**.

The model has produced:

```text
Tool Name:
multiply

Arguments:
a = 25
b = 40
```

---

# 11. Important: The Tool Has Not Been Executed Yet

This is the most common beginner misunderstanding.

After:

```python
response = llm_with_tools.invoke(...)
```

you might have:

```text
response.tool_calls
```

But that doesn't mean:

```python
multiply(25, 40)
```

has automatically executed.

The model has only said:

> "Please call this tool."

Something still needs to execute the request.

---

# 12. Step 6 — Tool Execution

Now your application reads the tool call:

```python
tool_call = response.tool_calls[0]
```

Then:

```python
result = multiply.invoke(
    tool_call["args"]
)
```

Conceptually:

```text
tool_call
   ↓
{
    "name": "multiply",
    "args": {
        "a": 25,
        "b": 40
    }
}
   ↓
multiply.invoke(...)
   ↓
1000
```

This is **Tool Execution**.

---

# 13. Step 7 — Tool Result

The tool returns:

```text
1000
```

But the process isn't necessarily finished.

The LLM needs to know:

> "What did my tool return?"

We send the result back as a tool message.

Conceptually:

```text
AIMessage
    ↓
ToolMessage
    ↓
LLM
```

---

# 14. Message Flow

This is one of the most important things to understand in LangChain.

A tool-calling conversation can look like:

```text
HumanMessage
    │
    │ "What is 25 × 40?"
    ▼
AIMessage
    │
    │ tool_calls:
    │ multiply(25,40)
    ▼
ToolMessage
    │
    │ 1000
    ▼
AIMessage
    │
    │ "25 × 40 = 1000"
    ▼
Final Answer
```

So the conversation contains multiple message types.

---

# 15. `AIMessage`

The LLM's response is usually represented as an `AIMessage`.

For example:

```text
AIMessage
```

may contain:

```python
{
    "tool_calls": [
        {
            "name": "multiply",
            "args": {
                "a": 25,
                "b": 40
            }
        }
    ]
}
```

This means:

> The AI wants to call the tool.

---

# 16. `ToolMessage`

After the application executes the tool:

```python
multiply.invoke({
    "a": 25,
    "b": 40
})
```

it gets:

```text
1000
```

That result is represented to the model as a tool message.

Conceptually:

```python
ToolMessage(
    content="1000",
    tool_call_id="call_123"
)
```

The `tool_call_id` is important because it associates the result with the corresponding tool request.

---

# 17. Why Does the Tool Result Go Back to the LLM?

Because the LLM needs to interpret the result.

For example:

```text
User:
What is 25 × 40?

LLM:
Call multiply(25,40)

Tool:
1000

LLM:
Therefore, the answer is 1000.
```

The tool itself doesn't necessarily generate the conversational response.

It simply returns data.

The LLM converts that data into a natural-language answer.

---

# 18. Complete Manual Flow

Conceptually, you can implement the entire process yourself:

```python
from langchain_core.messages import HumanMessage, ToolMessage

messages = [
    HumanMessage(
        content="What is 25 multiplied by 40?"
    )
]

# 1. Ask LLM
response = llm_with_tools.invoke(messages)

# 2. Add AI response
messages.append(response)

# 3. Execute requested tools
for tool_call in response.tool_calls:

    if tool_call["name"] == "multiply":

        result = multiply.invoke(
            tool_call["args"]
        )

        # 4. Add tool result
        messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
        )

# 5. Ask LLM again
final_response = llm_with_tools.invoke(messages)

print(final_response.content)
```

The exact implementation can vary with LangChain version, but the architecture is the important part.

---

# 19. Why Call the LLM Again?

Because the first LLM response was:

```text
"I need to call multiply."
```

The second LLM call gets:

```text
Tool Result:
1000
```

Now it can produce:

```text
25 × 40 = 1000.
```

So:

```text
LLM Call #1
→ Decide action

Tool
→ Execute action

LLM Call #2
→ Interpret result
```

---

# 20. Multiple Tool Calls

Now suppose we have:

```python
@tool
def add(a: int, b: int):
    """Add two numbers."""
    return a + b


@tool
def multiply(a: int, b: int):
    """Multiply two numbers."""
    return a * b
```

The model could potentially request:

```text
add(10, 20)
multiply(5, 6)
```

The application executes them:

```text
add(10,20)
    ↓
30

multiply(5,6)
    ↓
30
```

Then both results are returned to the LLM.

---

# 21. Sequential Tool Calling

Sometimes the second tool depends on the first tool's result.

Example:

```text
User:
Where is my order #123?
```

Available tools:

```text
get_order()
track_order()
```

The model may first call:

```text
get_order(123)
```

Result:

```json
{
    "tracking_id": "TRK999"
}
```

Now the model has the information required for the next call:

```text
track_order("TRK999")
```

Result:

```json
{
    "status": "In Transit",
    "location": "Delhi"
}
```

Then:

```text
LLM
 ↓
Final Answer
```

---

# 22. Tool Calling Loop

This gives us the basic agent loop:

```text
                 ┌─────────────┐
                 │    USER     │
                 └──────┬──────┘
                        ▼
                 ┌─────────────┐
                 │     LLM     │
                 └──────┬──────┘
                        │
                  Tool needed?
                   /          \
                 No            Yes
                 │              │
                 ▼              ▼
              Answer        Tool Call
                                │
                                ▼
                         Execute Tool
                                │
                                ▼
                           Tool Result
                                │
                                ▼
                               LLM
                                │
                         Another tool?
                         /          \
                       Yes          No
                        │            │
                        ▼            ▼
                     Tool         Answer
```

This is the conceptual foundation of an **AI Agent**.

---

# 23. Tool Calling Is Model-Level

Tool calling is primarily the model saying:

```text
"I want to invoke this function."
```

For example:

```json
{
    "name": "get_weather",
    "arguments": {
        "city": "Delhi"
    }
}
```

The model isn't necessarily making the HTTP request itself.

---

# 24. Tool Execution Is Application-Level

Your application might do:

```python
result = get_weather.invoke({
    "city": "Delhi"
})
```

or:

```python
result = requests.get(...)
```

or:

```python
result = db.orders.find(...)
```

or:

```python
result = python_executor.run(...)
```

The application is responsible for actually interacting with the outside world.

---

# 25. Why This Separation Is Important

This architecture provides security.

Imagine your agent has:

```text
send_email()
delete_database()
make_payment()
```

You don't want the LLM to have unrestricted access to your system.

Instead:

```text
LLM
 ↓
Tool Call
 ↓
Validation
 ↓
Authorization
 ↓
Human Approval
 ↓
Tool Execution
```

For example:

```text
LLM:
make_payment(amount=50000)

       ↓

Application:
Is this user authorized?

       ↓

Application:
Does amount exceed threshold?

       ↓

Human:
Approve payment?

       ↓

Tool Execution:
make_payment()
```

This is much safer.

---

# 26. Tool Execution Can Fail

Suppose:

```text
LLM
 ↓
get_customer(123)
 ↓
Database
```

Database returns:

```text
Connection Timeout
```

The tool result can communicate the failure.

Then the LLM may decide:

```text
Retry
```

or:

```text
Use another tool
```

or:

```text
Tell the user that the service is unavailable.
```

This is one reason tool results should contain useful error information.

---

# 27. Tool Calling With API

Suppose you create:

```python
@tool
def get_weather(city: str):
    """Get current weather for a city."""

    response = requests.get(
        f"https://api.weather.com/{city}"
    )

    return response.json()
```

The flow becomes:

```text
User
 ↓
"What's the weather in Delhi?"
 ↓
LLM
 ↓
Tool Call
get_weather("Delhi")
 ↓
Tool Execution
 ↓
HTTP Request
 ↓
Weather API
 ↓
JSON
 ↓
ToolMessage
 ↓
LLM
 ↓
"Delhi is currently 34°C."
```

---

# 28. Tool Calling With Database

Example:

```python
@tool
def get_customer(customer_id: int):
    """Retrieve customer information."""
    
    customer = collection.find_one({
        "customer_id": customer_id
    })

    return customer
```

Flow:

```text
User
 ↓
"What is customer 101's email?"
 ↓
LLM
 ↓
get_customer(101)
 ↓
MongoDB
 ↓
Customer document
 ↓
ToolMessage
 ↓
LLM
 ↓
Answer
```

---

# 29. Tool Calling With RAG

RAG retrieval can also be exposed as a tool.

For example:

```python
@tool
def search_documents(query: str):
    """Search company documentation."""
    return retriever.invoke(query)
```

Then:

```text
User
 ↓
LLM
 ↓
search_documents("refund policy")
 ↓
Vector DB
 ↓
Relevant documents
 ↓
ToolMessage
 ↓
LLM
 ↓
Answer
```

This is an important architecture for **Agentic RAG**.

---

# 30. Tool Calling vs Agent

This distinction is worth emphasizing.

### Tool Calling

You may have:

```text
LLM
 ↓
Tool Call
 ↓
Tool
 ↓
Result
```

You can manually control the loop.

### Agent

The framework manages the reasoning/action cycle:

```text
LLM
 ↓
Tool
 ↓
LLM
 ↓
Tool
 ↓
LLM
 ↓
Final Answer
```

An agent is essentially an orchestration layer around model reasoning and tool execution.

---

# 31. `bind_tools()` vs Tool Calling vs Execution

These three concepts should not be mixed up.

```text
@tool
   ↓
Creates Tool
```

```text
bind_tools()
   ↓
Makes Tool available to LLM
```

```text
LLM
   ↓
Generates tool_calls
```

```text
Application / Agent
   ↓
Executes tool
```

```text
Tool
   ↓
Returns result
```

```text
ToolMessage
   ↓
Returns result to LLM
```

---

# 32. Full Architecture

Memorize this:

```text
                ┌───────────────┐
                │     USER      │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │      LLM      │
                │               │
                │ Bound Tools   │
                └───────┬───────┘
                        │
                        ▼
                 TOOL CALLING
                        │
                        ▼
                ┌───────────────┐
                │  Tool Call    │
                │               │
                │ name          │
                │ arguments     │
                │ call_id       │
                └───────┬───────┘
                        │
                        ▼
               TOOL EXECUTION
                        │
              ┌─────────┼─────────┐
              ▼         ▼         ▼
            Python      API       DB
              │         │         │
              └─────────┼─────────┘
                        ▼
                  TOOL RESULT
                        │
                        ▼
                ┌───────────────┐
                │ ToolMessage   │
                └───────┬───────┘
                        │
                        ▼
                       LLM
                        │
                        ▼
                 FINAL ANSWER
```

---

# 33. Tool Calling vs Function Calling

You'll often see both terms:

```text
Function Calling
Tool Calling
```

Historically, **function calling** was commonly used for the model's structured request to call a function.

Modern agent frameworks more commonly use **tool calling**, because the callable capability doesn't have to be a simple local function. It can represent:

* APIs
* database operations
* search
* code execution
* retrievers
* external services
* application actions

So for LangChain, think primarily in terms of:

> **Tools + Tool Calling**

---

# 34. Real-World Example: E-Commerce Agent

Imagine your agent has:

```text
Tools:

search_products()
get_product()
check_inventory()
get_order()
track_order()
cancel_order()
```

User:

> Find a laptop under ₹80,000 and tell me if it is in stock.

The process could be:

### Tool Call 1

```text
search_products(
    category="laptop",
    max_price=80000
)
```

### Tool Execution

```text
Database
 ↓
Products
```

Result:

```json
[
    {
        "id": "P101",
        "name": "Lenovo Laptop",
        "price": 75000
    }
]
```

### Tool Call 2

```text
check_inventory(
    product_id="P101"
)
```

### Tool Execution

```text
Inventory DB
 ↓
25 units
```

### Final LLM response

```text
The Lenovo laptop costs ₹75,000 and is currently in stock with 25 units available.
```

Notice the agent used **two tools sequentially**.

---

# 35. Production Tool Execution Pipeline

In production, don't necessarily do:

```text
LLM → Tool → Result
```

A safer architecture is:

```text
LLM
 ↓
Tool Call
 ↓
Schema Validation
 ↓
Authentication
 ↓
Authorization
 ↓
Business Rules
 ↓
Human Approval (if required)
 ↓
Tool Execution
 ↓
Logging
 ↓
Tool Result
 ↓
LLM
```

For example, for a payment tool:

```text
make_payment()
```

you might require:

```text
✓ Valid amount
✓ Valid account
✓ User authorized
✓ Spending limit checked
✓ Fraud check
✓ Human confirmation
✓ Execute payment
✓ Audit log
```

---

# 36. The 6 Concepts You Should Master

For LangChain Agents, understand these in this order:

```text
1. Custom Tool
       ↓
2. @tool
       ↓
3. Tool Schema
       ↓
4. bind_tools()
       ↓
5. Tool Calling
       ↓
6. Tool Execution
       ↓
7. ToolMessage
       ↓
8. Agent Loop
```

The relationship is:

```text
Custom Function
      ↓
    @tool
      ↓
LangChain Tool
      ↓
bind_tools()
      ↓
LLM knows available tools
      ↓
Tool Calling
      ↓
tool_calls
      ↓
Tool Execution
      ↓
ToolMessage
      ↓
LLM
      ↓
Final Answer
```

---

## Final Interview Answer

If you're asked **"What is the difference between tool calling and tool execution?"**, answer:

> **Tool calling is the process where the LLM determines that a tool is required and generates a structured request containing the tool name and arguments. Tool execution is the subsequent process where the application or agent runtime actually invokes that tool, such as a Python function, API, database operation, or retriever. The execution result is then returned to the LLM as a tool message, allowing the model to continue reasoning and generate the final response.**

The next important topic after this is the **Agent Loop**, because the Agent Loop connects everything you've learned so far: **`bind_tools()` → `tool_calls` → tool execution → `ToolMessage` → LLM → another tool or final answer**.
