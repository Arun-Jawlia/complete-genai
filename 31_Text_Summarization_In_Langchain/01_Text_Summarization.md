# Text Summarization in LangChain

**Text summarization** means taking a long piece of text—such as a PDF, article, report, transcript, or document—and producing a shorter version that preserves the **important information and meaning**.

In LangChain, summarization becomes especially useful when the input is **larger than the model's context window** or when you want a structured summarization workflow.

---

## 1. Basic Idea

Suppose you have a large document:

```text
Long Document
     ↓
Load Document
     ↓
Split into Chunks
     ↓
Send Chunks to LLM
     ↓
Combine / Refine Summaries
     ↓
Final Summary
```

LangChain provides different strategies for handling this.

The three important approaches are:

1. **Stuff**
2. **Map-Reduce**
3. **Refine**

---

# 2. Stuff Method

The **Stuff** approach is the simplest.

All documents/chunks are placed into a **single prompt** and sent to the LLM.

```text
Document 1 ─┐
Document 2 ─┤
Document 3 ─┤
Document 4 ─┤ → LLM → Summary
Document 5 ─┘
```

### Example

Imagine we have:

```text
Chunk 1:
LangChain is a framework for developing applications powered by
language models...

Chunk 2:
LangChain provides components for prompts, models, retrievers...

Chunk 3:
LangChain can be used to build RAG applications...
```

Stuff combines everything:

```text
Chunk 1 + Chunk 2 + Chunk 3
              ↓
             LLM
              ↓
          Final Summary
```

### Code

Modern LangChain:

```python
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
Summarize the following documents.

Provide:
- Main ideas
- Important facts
- Key conclusions

Documents:

{context}
""")

chain = create_stuff_documents_chain(
    llm,
    prompt
)

result = chain.invoke({
    "context": documents
})

print(result)
```

### Advantage

Very simple:

```text
Documents → Prompt → LLM → Summary
```

### Problem

All documents must fit inside the model's context window.

For example:

```text
100-page PDF
     ↓
100 pages into one prompt
     ↓
Context limit ❌
```

So Stuff is best for **small or moderate-sized documents**.

---

# 3. Map-Reduce Method

For large documents, **Map-Reduce** is much more useful.

The document is divided into chunks.

Each chunk is summarized independently.

```text
                 Document
                    ↓
             Split into chunks
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
    Chunk 1      Chunk 2      Chunk 3
       ↓            ↓            ↓
    Summary 1    Summary 2    Summary 3
       └────────────┼────────────┘
                    ↓
              Combine summaries
                    ↓
                   LLM
                    ↓
             Final Summary
```

### Map phase

Each chunk gets summarized independently.

```text
Chunk 1 → Summary 1
Chunk 2 → Summary 2
Chunk 3 → Summary 3
```

This is the **Map** step.

### Reduce phase

The individual summaries are combined.

```text
Summary 1
Summary 2
Summary 3
     ↓
   LLM
     ↓
Final Summary
```

This is the **Reduce** step.

---

## 4. Why Map-Reduce is Powerful

Imagine a 500-page book.

You don't want:

```text
500 pages → one LLM request
```

Instead:

```text
500 pages
   ↓
100 chunks
   ↓
100 individual summaries
   ↓
Combine summaries
   ↓
Final summary
```

This allows you to handle **much larger documents**.

---

# 5. Refine Method

The **Refine** approach summarizes the document sequentially.

The first chunk creates an initial summary.

Then the next chunk is used to **improve/refine** that summary.

```text
Chunk 1
  ↓
Initial Summary
  ↓
+ Chunk 2
  ↓
Refined Summary
  ↓
+ Chunk 3
  ↓
Refined Summary
  ↓
+ Chunk 4
  ↓
Final Summary
```

For example:

```text
Chunk 1
↓
"The document discusses AI."

Chunk 2
↓
"Add information about RAG."

Chunk 3
↓
"Add information about AI agents."

Final:
"The document discusses AI, RAG and AI agents..."
```

---

# 6. Refine vs Map-Reduce

The key difference is:

### Map-Reduce

Each chunk is processed independently.

```text
Chunk 1 → Summary 1 ─┐
Chunk 2 → Summary 2 ─┤
Chunk 3 → Summary 3 ─┤ → Final Summary
Chunk 4 → Summary 4 ─┘
```

### Refine

The summary is continuously updated.

```text
Chunk 1 → Summary
            ↓
Chunk 2 → Refined Summary
            ↓
Chunk 3 → Refined Summary
            ↓
Chunk 4 → Final Summary
```

---

# 7. Comparison

| Method         | How it works                                 | Best for           | Main Problem          |
| -------------- | -------------------------------------------- | ------------------ | --------------------- |
| **Stuff**      | Put everything into one prompt               | Small documents    | Context limit         |
| **Map-Reduce** | Summarize chunks independently, then combine | Large documents    | More LLM calls        |
| **Refine**     | Sequentially improve summary                 | Detailed summaries | Sequential and slower |

---

# 8. Complete Summarization Pipeline

A real-world LangChain summarization system might look like this:

```text
                 PDF
                  ↓
           Document Loader
                  ↓
          Recursive Splitter
                  ↓
          ┌───────┴───────┐
          ↓               ↓
       Chunk 1          Chunk N
          ↓               ↓
        LLM               LLM
          ↓               ↓
     Summary 1        Summary N
          └───────┬───────┘
                  ↓
            Reduce / Refine
                  ↓
             Final Summary
```

For example:

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
```

Load the PDF:

```python
loader = PyPDFLoader("document.pdf")

documents = loader.load()
```

Split it:

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)
```

Now you have:

```text
documents
    ↓
chunks
    ↓
[chunk1, chunk2, chunk3, ...]
```

Then pass those chunks into your summarization chain.

---

# 9. Summarization Prompt

A good summarization prompt is important.

For example:

```text
You are an expert summarizer.

Summarize the provided text while preserving:
1. Main ideas
2. Important facts
3. Key arguments
4. Important conclusions

Do not introduce information that is not present
in the original text.

Text:
{context}
```

You can also request a particular format:

```text
Summarize the document using:

## Overview
## Key Points
## Important Facts
## Conclusion

Keep the summary concise but informative.
```

---

# 10. Summarization vs RAG

This distinction is **very important for a GenAI Engineer**.

### Summarization

You want to understand the **whole document**.

```text
PDF
 ↓
Chunks
 ↓
LLM
 ↓
Summary
```

Example:

> "Summarize this 100-page annual report."

---

### RAG

You want to answer a **specific question** using the document.

```text
PDF
 ↓
Chunks
 ↓
Embeddings
 ↓
Vector Database
 ↓
Retriever
 ↓
Relevant Chunks
 ↓
LLM
 ↓
Answer
```

Example:

> "What was the company's revenue in 2025?"

So:

**Summarization = compress information**

**RAG = retrieve relevant information**

---

# 11. Important LangChain Components

When building summarization applications, you'll commonly work with:

```text
Document Loader
       ↓
Text Splitter
       ↓
Document
       ↓
Prompt Template
       ↓
Chat Model
       ↓
Chain
       ↓
Output Parser
```

For example:

```python
PDFLoader
    ↓
RecursiveCharacterTextSplitter
    ↓
ChatPromptTemplate
    ↓
ChatOpenAI
    ↓
Summarization Chain
    ↓
StrOutputParser
```

---

# 12. Production-Level Considerations

When building a real summarization application, don't only think about the prompt.

Consider:

### Context size

How much text can the model process?

### Token cost

Map-Reduce can make many LLM calls.

### Latency

Refine can be slower because calls happen sequentially.

### Information loss

Repeated summarization can lose small but important details.

### Chunk size

Too small:

```text
Context is incomplete
```

Too large:

```text
More tokens + possible context problems
```

### Chunk overlap

Overlap helps preserve information across boundaries.

For example:

```text
Chunk 1: A B C D E
Chunk 2:       D E F G H
```

instead of:

```text
Chunk 1: A B C D E
Chunk 2: F G H I J
```

---

# 13. Interview Definition

If an interviewer asks:

> **What is text summarization in LangChain?**

A strong answer would be:

**"Text summarization in LangChain is the process of using LangChain's document processing, prompting, and LLM components to convert long documents into concise summaries. For small documents, the Stuff strategy can send all content to the model at once, while Map-Reduce processes chunks independently and then combines their summaries, and Refine iteratively improves a summary as it processes each chunk."**

---

## Mental Model

Remember this:

```text
                TEXT SUMMARIZATION
                       │
             ┌─────────┼─────────┐
             │         │         │
           Stuff    Map-Reduce  Refine
             │         │         │
             │         │         │
         All at once  Parallel   Sequential
             │         │         │
             ↓         ↓         ↓
           Small      Large     Detailed
         documents  documents   summaries
```

For your **LangChain learning path**, I would learn summarization in this order:

**Stuff → Map-Reduce → Refine → Document Summarization → PDF Summarizer → Long-document summarization → RAG vs Summarization**.
