# Refine Summarization Chain in LangChain

The **Refine Summarization Chain** is a document summarization strategy where the LLM creates an **initial summary from the first chunk** and then **iteratively improves that summary using each subsequent chunk**.

The core idea is:

> **Create a summary → read the next chunk → refine the existing summary → repeat until all chunks are processed.**

---

## 1. The Basic Idea

Suppose we have a large document divided into 4 chunks:

```text
Document
   ↓
┌────────┬────────┬────────┬────────┐
│ Chunk 1│ Chunk 2│ Chunk 3│ Chunk 4│
└────────┴────────┴────────┴────────┘
```

Refine processes them **sequentially**:

```text
Chunk 1
   ↓
LLM
   ↓
Initial Summary
   ↓
+ Chunk 2
   ↓
LLM
   ↓
Refined Summary
   ↓
+ Chunk 3
   ↓
LLM
   ↓
Refined Summary
   ↓
+ Chunk 4
   ↓
LLM
   ↓
Final Summary
```

So unlike Map-Reduce, the summary is **continuously carried forward**.

---

# 2. Simple Example

Imagine a document about a company.

### Chunk 1

```text
The company was founded in 2010 by three engineers.
```

LLM creates:

```text
Summary:
The company was founded in 2010 by three engineers.
```

---

### Chunk 2

```text
In 2015, the company expanded into international markets.
```

Now the LLM receives:

```text
Existing Summary:
The company was founded in 2010 by three engineers.

New Information:
In 2015, the company expanded into international markets.
```

It refines the summary:

```text
The company was founded in 2010 by three engineers
and expanded into international markets in 2015.
```

---

### Chunk 3

```text
In 2020, the company launched an AI research division.
```

LLM receives:

```text
Existing Summary:
The company was founded in 2010 by three engineers
and expanded internationally in 2015.

New Information:
In 2020, the company launched an AI research division.
```

New refined summary:

```text
The company was founded in 2010 by three engineers,
expanded internationally in 2015, and launched an
AI research division in 2020.
```

That's the **Refine strategy**.

---

# 3. Refine Architecture

```text
                    DOCUMENT
                       ↓
                 Split into chunks
                       ↓
                    Chunk 1
                       ↓
                      LLM
                       ↓
               Initial Summary
                       ↓
                 ┌─────┴─────┐
                 │           │
              Chunk 2     Existing
                 │         Summary
                 └─────┬─────┘
                       ↓
                      LLM
                       ↓
               Refined Summary
                       ↓
                 ┌─────┴─────┐
                 │           │
              Chunk 3     Existing
                 │         Summary
                 └─────┬─────┘
                       ↓
                      LLM
                       ↓
               Refined Summary
                       ↓
                     ...
                       ↓
                 Final Summary
```

---

# 4. Refine Has Two Main Prompts

This is an important LangChain concept.

You generally need:

### 1. Initial prompt

Used for the **first chunk**.

```text
Document Chunk
     ↓
Initial Prompt
     ↓
LLM
     ↓
Initial Summary
```

### 2. Refine prompt

Used for **every subsequent chunk**.

```text
Existing Summary + New Chunk
             ↓
        Refine Prompt
             ↓
             LLM
             ↓
      Updated Summary
```

---

# 5. Initial Prompt

A typical initial prompt could be:

```python
initial_prompt = ChatPromptTemplate.from_template("""
You are an expert document summarizer.

Create a concise summary of the following document.

Focus on:
- Main ideas
- Important facts
- Key arguments
- Important conclusions

Document:
{context}
""")
```

The important variable here is:

```text
{context}
```

because it represents the first document chunk.

---

# 6. Refine Prompt

The refine prompt needs **two pieces of information**:

```text
1. Existing summary
2. New document chunk
```

For example:

```python
refine_prompt = ChatPromptTemplate.from_template("""
You are refining an existing summary.

Existing summary:
{existing_answer}

New document content:
{context}

Update the existing summary using the new information.

Instructions:
- Preserve important information from the existing summary.
- Add important information from the new content.
- Remove unnecessary repetition.
- Keep the summary concise.
- Do not introduce information not present in the documents.

Refined summary:
""")
```

Notice the two variables:

```text
{existing_answer}
{context}
```

---

# 7. The Most Important Variable

The key concept in Refine is:

```text
existing_answer
```

This represents the summary generated so far.

For example:

```text
Iteration 1:

existing_answer = None
context = Chunk 1

          ↓
        LLM

existing_answer = Summary 1
```

Then:

```text
Iteration 2:

existing_answer = Summary 1
context = Chunk 2

          ↓
        LLM

existing_answer = Summary 2
```

Then:

```text
Iteration 3:

existing_answer = Summary 2
context = Chunk 3

          ↓
        LLM

existing_answer = Summary 3
```

And so on.

---

# 8. Refine as a Loop

You can mentally understand Refine like this:

```python
summary = summarize(chunk_1)

for chunk in remaining_chunks:
    summary = refine(
        existing_summary=summary,
        new_chunk=chunk
    )
```

That's essentially what the Refine chain is doing.

The important part is:

```text
summary → next iteration → updated summary
```

---

# 9. Conceptual Python Implementation

Before using LangChain's higher-level chain abstraction, it's useful to understand the logic manually:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

### Initial chain

```python
initial_prompt = ChatPromptTemplate.from_template("""
Summarize this document chunk:

{context}
""")

initial_chain = initial_prompt | llm
```

### Refine chain

```python
refine_prompt = ChatPromptTemplate.from_template("""
Existing summary:
{existing_answer}

New document chunk:
{context}

Refine the existing summary using the new information.
""")

refine_chain = refine_prompt | llm
```

Then conceptually:

```python
response = initial_chain.invoke({
    "context": chunks[0].page_content
})

summary = response.content

for chunk in chunks[1:]:

    response = refine_chain.invoke({
        "existing_answer": summary,
        "context": chunk.page_content
    })

    summary = response.content

print(summary)
```

This code makes the Refine mechanism very clear.

---

# 10. Refine vs Map-Reduce

This is one of the most important comparisons.

## Map-Reduce

Each chunk is processed independently.

```text
Chunk 1 → LLM → Summary 1 ─┐
Chunk 2 → LLM → Summary 2 ─┤
Chunk 3 → LLM → Summary 3 ─┤
Chunk 4 → LLM → Summary 4 ─┘
                            ↓
                           LLM
                            ↓
                       Final Summary
```

There is **no dependency between the individual map operations**.

---

## Refine

Each iteration depends on the previous result.

```text
Chunk 1 → LLM → Summary 1
                    ↓
Chunk 2 ────────────┤
                    ↓
                   LLM
                    ↓
                 Summary 2
                    ↓
Chunk 3 ────────────┤
                    ↓
                   LLM
                    ↓
                 Summary 3
```

So:

### Map-Reduce

**Parallel-friendly**

```text
Chunk 1 ─┐
Chunk 2 ─┤
Chunk 3 ─┤ → Reduce
Chunk 4 ─┘
```

### Refine

**Sequential**

```text
Chunk 1
  ↓
Chunk 2
  ↓
Chunk 3
  ↓
Chunk 4
```

---

# 11. Refine vs Stuff

### Stuff

All documents are sent together:

```text
Chunk 1 ─┐
Chunk 2 ─┤
Chunk 3 ─┤ → ONE LLM CALL → Summary
Chunk 4 ─┘
```

### Refine

Documents are processed one at a time:

```text
Chunk 1 → LLM
           ↓
        Summary
           ↓
Chunk 2 → LLM
           ↓
        Summary
           ↓
Chunk 3 → LLM
           ↓
        Summary
```

---

# 12. Comparison Table

| Feature                    | Stuff       | Map-Reduce         | Refine                         |
| -------------------------- | ----------- | ------------------ | ------------------------------ |
| Processing                 | All at once | Independent chunks | Sequential chunks              |
| LLM calls                  | Low         | High               | High                           |
| Large documents            | ⚠️ Limited  | ✅ Excellent        | ✅ Good                         |
| Parallelization            | N/A         | ✅ Easy             | ❌ Difficult                    |
| Maintains evolving context | ❌           | ❌                  | ✅                              |
| Complexity                 | Low         | Medium             | Medium                         |
| Best for                   | Small docs  | Large docs         | Incremental/detailed summaries |

---

# 13. When Should You Use Refine?

Refine is useful when **later sections can add important context to the existing summary**.

For example:

### Books

```text
Chapter 1
   ↓
Initial Summary
   ↓
Chapter 2
   ↓
Refine
   ↓
Chapter 3
   ↓
Refine
```

### Research papers

```text
Abstract
   ↓
Introduction
   ↓
Methodology
   ↓
Results
   ↓
Conclusion
```

A refined summary can gradually incorporate the important information from each section.

### Meeting transcripts

```text
Part 1 → Summary
Part 2 → Refine
Part 3 → Refine
Part 4 → Refine
```

---

# 14. Advantages

### 1. Incremental understanding

The summary evolves as new information arrives.

### 2. Can handle large documents

You don't have to put the entire document into one prompt.

### 3. Preserves previous context

The LLM receives the existing summary while processing new information.

### 4. Good for sequential information

If the order of the document matters, Refine can be useful.

For example:

```text
Problem
 ↓
Method
 ↓
Experiment
 ↓
Result
 ↓
Conclusion
```

---

# 15. Disadvantages

The biggest problem is **latency**.

Suppose you have:

```text
100 chunks
```

Refine might require approximately:

```text
1 initial LLM call
+
99 refinement calls
=
100 LLM calls
```

And because each refinement depends on the previous one:

```text
Call 1
 ↓
Call 2
 ↓
Call 3
 ↓
Call 4
 ↓
...
```

you can't simply execute all of them simultaneously.

---

# 16. Another Important Problem: Summary Drift

Consider:

```text
Chunk 1
 ↓
Summary 1
 ↓
Chunk 2
 ↓
Summary 2
 ↓
Chunk 3
 ↓
Summary 3
 ↓
...
 ↓
Summary 50
```

Every iteration is modifying the previous summary.

This can potentially cause:

```text
Original information
       ↓
Summary
       ↓
Compressed summary
       ↓
More compressed summary
       ↓
Information loss
```

So your refine prompt should explicitly tell the model:

```text
Preserve important information from the existing summary.
Do not remove important facts unless they are contradicted
or clearly irrelevant.
```

---

# 17. Refine with a PDF

A real application could look like:

```text
                  PDF
                   ↓
             PyPDFLoader
                   ↓
                Pages
                   ↓
        RecursiveCharacterSplitter
                   ↓
                Chunks
                   ↓
          ┌────────┴────────┐
          │                 │
       Chunk 1           Chunk 2...
          │                 │
          ↓                 ↓
   Initial Prompt       Refine Prompt
          │                 │
          ↓                 │
         LLM ←──────────────┘
          │
          ↓
     Initial Summary
          │
          ↓
      Refined Summary
          │
          ↓
      Refined Summary
          │
          ↓
      Final Summary
```

---

# 18. The Most Important Mental Model

Don't think of Refine as:

```text
Chunk → Summary
```

Think:

```text
                ┌───────────────┐
                │ Existing      │
                │ Summary       │
                └───────┬───────┘
                        │
                        │
New Chunk ───────────────┤
                        ↓
                       LLM
                        ↓
                Updated Summary
                        │
                        └───────────────┐
                                        │
New Chunk ──────────────────────────────┤
                                        ↓
                                       LLM
                                        ↓
                                Updated Summary
```

The **previous summary becomes the input for the next iteration**.

---

# 19. Interview Answer

If an interviewer asks:

> **What is the Refine summarization chain in LangChain?**

You can answer:

> **"The Refine summarization chain processes documents sequentially. It first generates an initial summary from the first document chunk, then passes that summary along with the next chunk to the LLM to refine it. This process continues for every subsequent chunk until a final summary is produced. Unlike Map-Reduce, where chunks can be processed independently, Refine maintains an evolving summary and therefore is inherently sequential."**

---

## Final Cheat Sheet

```text
STUFF
────────────────────────
All chunks
     ↓
One prompt
     ↓
LLM
     ↓
Final Summary


MAP-REDUCE
────────────────────────
Chunks
 ↓
LLM individually
 ↓
Individual summaries
 ↓
LLM
 ↓
Final Summary


REFINE
────────────────────────
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

### One-line memory trick:

**Stuff = combine everything.**

**Map-Reduce = summarize separately, then combine.**

**Refine = summarize, then continuously improve the summary.**
