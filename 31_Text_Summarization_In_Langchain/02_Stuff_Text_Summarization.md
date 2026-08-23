# Stuff Text Summarization in LangChain

**Stuff summarization** is the simplest document-summarization strategy in LangChain.

The basic idea is:

> **Take all the documents/chunks, put ("stuff") them into one prompt, and send that prompt to the LLM to generate a single summary.**

---

## 1. Basic Architecture

```text
Documents
   │
   ├── Document 1
   ├── Document 2
   ├── Document 3
   └── Document 4
          │
          ▼
    Combine documents
          │
          ▼
       Prompt
          │
          ▼
         LLM
          │
          ▼
    Final Summary
```

For example, suppose you have three documents:

```text
Document 1:
LangChain is a framework for building LLM applications.

Document 2:
LangChain provides components for prompts, models,
retrievers and document processing.

Document 3:
LangChain can be used to build RAG and agent applications.
```

Stuff combines them:

```text
Document 1
Document 2
Document 3
     ↓
One Prompt
     ↓
LLM
     ↓
"LangChain is a framework for building LLM applications
with components for prompts, retrieval and agents."
```

---

# 2. Why is it called "Stuff"?

Because we **stuff all the document content into the prompt**.

Conceptually:

```python
prompt = """
Summarize the following documents:

{documents}
"""
```

If we have:

```python
documents = [
    document1,
    document2,
    document3
]
```

LangChain essentially creates:

```text
Prompt
─────────────────────────────

Summarize the following documents:

Document 1 content...

Document 2 content...

Document 3 content...

─────────────────────────────
```

Then:

```text
Prompt → LLM → Summary
```

---

# 3. When Should You Use Stuff?

Stuff is best when the total document content is small enough to fit within the model's context window.

### Good use case

```text
10-page document
       ↓
Stuff
       ↓
LLM
       ↓
Summary
```

### Bad use case

```text
1000-page book
       ↓
Stuff everything
       ↓
LLM
       ↓
❌ Context too large
```

For very large documents, **Map-Reduce** or **Refine** is usually more appropriate.

---

# 4. Stuff vs Map-Reduce

This is an important distinction.

### Stuff

```text
Chunk 1 ─┐
Chunk 2 ─┤
Chunk 3 ─┤
Chunk 4 ─┤
Chunk 5 ─┘
    ↓
   LLM
    ↓
Summary
```

**One main LLM call** for the combined documents.

### Map-Reduce

```text
Chunk 1 → LLM → Summary 1
Chunk 2 → LLM → Summary 2
Chunk 3 → LLM → Summary 3
Chunk 4 → LLM → Summary 4
                     ↓
                  LLM
                     ↓
              Final Summary
```

Multiple calls.

So:

| Feature            | Stuff         | Map-Reduce          |
| ------------------ | ------------- | ------------------- |
| LLM calls          | Usually 1     | Multiple            |
| Simplicity         | Very easy     | More complex        |
| Small documents    | ✅ Excellent   | Usually unnecessary |
| Large documents    | ❌ Limited     | ✅ Good              |
| Cost               | Lower         | Higher              |
| Context limitation | Major concern | Much less           |

---

# 5. Implementing Stuff in LangChain

A modern LangChain implementation can use:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
```

Create the model:

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

Create the prompt:

```python
prompt = ChatPromptTemplate.from_template("""
You are an expert text summarizer.

Summarize the following documents.

Focus on:
- Main ideas
- Important facts
- Key conclusions

Documents:
{context}
""")
```

Create the Stuff document chain:

```python
chain = create_stuff_documents_chain(
    llm,
    prompt
)
```

Then invoke it:

```python
result = chain.invoke({
    "context": documents
})

print(result)
```

---

# 6. Understanding `{context}`

This is one of the most important concepts.

You write:

```python
{context}
```

inside your prompt.

LangChain expects the documents to be supplied using the `context` variable:

```python
chain.invoke({
    "context": documents
})
```

LangChain then formats the documents and inserts their content into the prompt.

Conceptually:

```text
documents
    ↓
Document contents extracted
    ↓
"context"
    ↓
Prompt
    ↓
LLM
```

---

# 7. What is a `Document`?

LangChain typically represents documents using the `Document` object.

For example:

```python
from langchain_core.documents import Document

documents = [
    Document(
        page_content="LangChain is a framework for building LLM applications.",
        metadata={"source": "intro.txt"}
    ),
    Document(
        page_content="LangChain provides tools for retrieval and agents.",
        metadata={"source": "features.txt"}
    )
]
```

A `Document` contains mainly:

```text
Document
├── page_content
└── metadata
```

For summarization, the important part is:

```python
document.page_content
```

---

# 8. Complete Example

Let's create a simple example without a PDF.

```python
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
```

### Step 1 — Create documents

```python
documents = [
    Document(
        page_content="""
        LangChain is a framework designed for developing
        applications powered by large language models.
        """
    ),

    Document(
        page_content="""
        It provides abstractions for prompts, models,
        document loaders, retrievers and output parsers.
        """
    ),

    Document(
        page_content="""
        LangChain can be used to develop applications
        such as RAG systems, chatbots and AI agents.
        """
    )
]
```

### Step 2 — Create LLM

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

### Step 3 — Create prompt

```python
prompt = ChatPromptTemplate.from_template("""
Summarize the following documents in 3-4 sentences.

Documents:
{context}
""")
```

### Step 4 — Create Stuff chain

```python
chain = create_stuff_documents_chain(
    llm,
    prompt
)
```

### Step 5 — Run

```python
summary = chain.invoke({
    "context": documents
})

print(summary)
```

The flow is:

```text
Document 1 ─┐
Document 2 ─┼──→ create_stuff_documents_chain
Document 3 ─┘              │
                           ↓
                         Prompt
                           ↓
                          LLM
                           ↓
                        Summary
```

---

# 9. Stuff with a PDF

This becomes more useful in a real application.

```text
PDF
 ↓
PyPDFLoader
 ↓
Documents
 ↓
Stuff Chain
 ↓
LLM
 ↓
Summary
```

Example:

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("research-paper.pdf")

documents = loader.load()
```

Now:

```python
summary = chain.invoke({
    "context": documents
})
```

The problem is that a large PDF might contain too many tokens.

Therefore, you might first split it:

```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)
```

Then:

```python
summary = chain.invoke({
    "context": chunks
})
```

But remember: **splitting does not magically remove the Stuff context limitation**.

If you have:

```text
100 chunks × 2,000 characters
```

you're still attempting to put all of them into one LLM request.

---

# 10. Prompt Design

The quality of Stuff summarization depends heavily on the prompt.

A basic prompt:

```python
prompt = ChatPromptTemplate.from_template("""
Summarize the following content:

{context}
""")
```

A better prompt:

```python
prompt = ChatPromptTemplate.from_template("""
You are an expert document summarizer.

Summarize the provided content.

Requirements:
- Identify the main topic.
- Extract the most important points.
- Preserve important facts and numbers.
- Remove unnecessary repetition.
- Do not introduce information not present in the source.
- Keep the summary concise.

Content:
{context}
""")
```

You can also control the output:

```python
prompt = ChatPromptTemplate.from_template("""
Summarize the following document.

Return the result using this structure:

## Overview
A short overview.

## Key Points
- Point 1
- Point 2
- Point 3

## Conclusion
A concise conclusion.

Document:
{context}
""")
```

---

# 11. Important Limitation

The biggest weakness of Stuff is the **context window**.

Suppose:

```text
Document = 500,000 tokens
Model context = 128,000 tokens
```

You cannot simply do:

```python
chain.invoke({
    "context": documents
})
```

because the combined prompt can exceed the model's context capacity.

That's where:

```text
Stuff
   ↓
Map-Reduce
   ↓
Refine
```

becomes an important progression.

---

# 12. Stuff Summarization Mental Model

Remember this simple formula:

```text
                    STUFF
                      │
        ┌─────────────┴─────────────┐
        │                           │
   Multiple Docs              One Prompt
        │                           │
        └─────────────┬─────────────┘
                      ↓
                     LLM
                      ↓
                 One Summary
```

Or simply:

> **Stuff = Combine everything → put it in one prompt → call the LLM → get the summary.**

---

## Interview Answer

If asked **"What is Stuff summarization in LangChain?"**, say:

> **"Stuff is a document-combination strategy in LangChain where all documents are inserted into a single prompt and passed to the LLM in one request to generate the final summary. It is simple and effective for documents that fit within the model's context window, but it becomes unsuitable for very large documents because the combined content can exceed the context limit."**

That is the core concept you should remember.
