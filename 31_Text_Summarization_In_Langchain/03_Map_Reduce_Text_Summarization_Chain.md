# Map-Reduce Summarization Chain in LangChain

**Map-Reduce summarization** is a technique used to summarize **large documents** that cannot be safely passed to an LLM in a single prompt.

The core idea is:

> **First summarize each chunk independently (Map), then combine those summaries and generate a final summary (Reduce).**

---

# 1. Why Do We Need Map-Reduce?

Suppose you have a 300-page PDF.

With **Stuff**, you would do:

```text
300-page PDF
     ↓
Put everything into one prompt
     ↓
LLM
     ↓
Summary
```

This can fail because the document may exceed the model's context window.

With Map-Reduce:

```text
                300-page PDF
                      ↓
                 Split into chunks
                      ↓
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
     Chunk 1       Chunk 2       Chunk 3 ...
        ↓             ↓             ↓
      LLM            LLM            LLM
        ↓             ↓             ↓
   Summary 1      Summary 2      Summary 3
        └─────────────┼─────────────┘
                      ↓
               Combine summaries
                      ↓
                     LLM
                      ↓
                Final Summary
```

This gives us two major stages:

```text
MAP
 ↓
Summarize each chunk

REDUCE
 ↓
Combine those summaries
```

---

# 2. The Map Step

The **Map step** takes every document/chunk independently.

For example:

```text
Chunk 1 → LLM → Summary 1

Chunk 2 → LLM → Summary 2

Chunk 3 → LLM → Summary 3

Chunk 4 → LLM → Summary 4
```

Imagine a book:

### Chunk 1

```text
The company was founded in 2010...
```

LLM produces:

```text
Summary 1:
The company was founded in 2010.
```

### Chunk 2

```text
The company expanded internationally in 2015...
```

LLM produces:

```text
Summary 2:
The company expanded internationally in 2015.
```

### Chunk 3

```text
The company launched its AI division in 2020...
```

LLM produces:

```text
Summary 3:
The company launched an AI division in 2020.
```

So:

```text
Chunk 1 → Summary 1
Chunk 2 → Summary 2
Chunk 3 → Summary 3
```

That's **Map**.

---

# 3. The Reduce Step

Now we have:

```text
Summary 1
Summary 2
Summary 3
Summary 4
```

We combine them:

```text
Summary 1 ─┐
Summary 2 ─┤
Summary 3 ─┤ → LLM → Final Summary
Summary 4 ─┘
```

The LLM receives the intermediate summaries and creates one coherent final summary.

For example:

```text
Summary 1:
Company founded in 2010.

Summary 2:
Expanded internationally in 2015.

Summary 3:
Launched AI division in 2020.
```

Reduce produces:

```text
Final Summary:

The company was founded in 2010, expanded internationally
in 2015, and launched its AI division in 2020.
```

---

# 4. Complete Architecture

The entire chain looks like this:

```text
                    DOCUMENT
                       │
                       ▼
                Document Loader
                       │
                       ▼
                Text Splitter
                       │
                       ▼
              ┌─────────────────┐
              │     MAP STEP    │
              └─────────────────┘
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Chunk 1      Chunk 2      Chunk 3
          ↓            ↓            ↓
         LLM          LLM          LLM
          ↓            ↓            ↓
      Summary 1    Summary 2    Summary 3
          └────────────┼────────────┘
                       ↓
              ┌─────────────────┐
              │   REDUCE STEP   │
              └─────────────────┘
                       ↓
                Combine summaries
                       ↓
                      LLM
                       ↓
                FINAL SUMMARY
```

---

# 5. LangChain Components

A Map-Reduce summarization chain generally has two important chains:

### Map chain

```text
Document → Prompt → LLM → Summary
```

### Reduce chain

```text
Summaries → Prompt → LLM → Final Summary
```

Conceptually:

```python
map_chain = ...

reduce_chain = ...

map_reduce_chain = ...
```

---

# 6. Creating the Map Chain

Let's start with the LLM:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

Now create the map prompt:

```python
from langchain_core.prompts import ChatPromptTemplate

map_prompt = ChatPromptTemplate.from_template("""
You are an expert summarizer.

Summarize the following document chunk.

Focus on:
- Important facts
- Main ideas
- Key arguments
- Important conclusions

Document:
{context}
""")
```

Then create the map chain:

```python
from langchain_core.output_parsers import StrOutputParser

map_chain = map_prompt | llm | StrOutputParser()
```

So:

```text
Document Chunk
      ↓
map_prompt
      ↓
LLM
      ↓
String Output
```

---

# 7. Creating the Reduce Chain

Now we need another prompt.

```python
reduce_prompt = ChatPromptTemplate.from_template("""
You are an expert summarizer.

You have been given summaries of different parts
of a larger document.

Combine these summaries into one coherent final summary.

Requirements:
- Remove duplicate information.
- Preserve important facts.
- Maintain logical flow.
- Do not introduce information that isn't present.
- Keep the final summary concise but informative.

Summaries:

{context}
""")
```

Then:

```python
reduce_chain = reduce_prompt | llm | StrOutputParser()
```

Architecture:

```text
Summaries
    ↓
reduce_prompt
    ↓
LLM
    ↓
Final Summary
```

---

# 8. The Important Part: Mapping

Suppose:

```python
chunks = [
    chunk1,
    chunk2,
    chunk3,
    chunk4
]
```

We run the map chain on every chunk:

```python
summaries = []

for chunk in chunks:
    summary = map_chain.invoke({
        "context": chunk.page_content
    })

    summaries.append(summary)
```

Now:

```text
chunks
   ↓
┌──────┬──────┬──────┬──────┐
│ C1   │ C2   │ C3   │ C4   │
└──────┴──────┴──────┴──────┘
   ↓      ↓      ↓      ↓
  LLM    LLM    LLM    LLM
   ↓      ↓      ↓      ↓
  S1     S2     S3     S4
```

---

# 9. Reduce the Summaries

Now combine the summaries:

```python
combined_summaries = "\n\n".join(summaries)
```

Then:

```python
final_summary = reduce_chain.invoke({
    "context": combined_summaries
})
```

And finally:

```python
print(final_summary)
```

---

# 10. Complete Simple Implementation

Here's the conceptual implementation:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------------
# LLM
# -------------------------

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# -------------------------
# MAP
# -------------------------

map_prompt = ChatPromptTemplate.from_template("""
Summarize the following document chunk.

Focus on the most important information.

Document:
{context}
""")

map_chain = map_prompt | llm | StrOutputParser()


# -------------------------
# REDUCE
# -------------------------

reduce_prompt = ChatPromptTemplate.from_template("""
Combine the following summaries into one
coherent final summary.

Remove repetition and preserve important information.

Summaries:
{context}
""")

reduce_chain = reduce_prompt | llm | StrOutputParser()


# -------------------------
# MAP STEP
# -------------------------

summaries = []

for chunk in chunks:

    summary = map_chain.invoke({
        "context": chunk.page_content
    })

    summaries.append(summary)


# -------------------------
# REDUCE STEP
# -------------------------

combined_summaries = "\n\n".join(summaries)

final_summary = reduce_chain.invoke({
    "context": combined_summaries
})

print(final_summary)
```

This demonstrates the **core Map-Reduce concept**.

---

# 11. Using LangChain's Document Chains

LangChain also provides document-combination abstractions so you don't have to manually implement everything.

The conceptual structure is:

```text
Map Chain
    ↓
Each Document
    ↓
Intermediate Summaries
    ↓
Reduce Documents Chain
    ↓
Final Summary
```

Depending on the LangChain version, APIs around document-combination chains can change, so it's important to distinguish the **concept** from a specific helper function.

The important architecture remains:

```text
map_chain
    +
reduce_chain
    ↓
map-reduce summarization
```

---

# 12. Map-Reduce vs Stuff

This is extremely important.

### Stuff

```text
Chunk 1 ─┐
Chunk 2 ─┤
Chunk 3 ─┤
Chunk 4 ─┘
    ↓
   LLM
    ↓
Summary
```

One large LLM call.

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

Multiple LLM calls.

---

# 13. Major Advantage

The biggest advantage is **handling large documents**.

Suppose:

```text
Total document = 500,000 tokens
```

You split it into:

```text
500 chunks × 1,000 tokens
```

Map processes each chunk separately:

```text
1,000 tokens → LLM
1,000 tokens → LLM
1,000 tokens → LLM
...
```

Then the reduce step processes the **shorter intermediate summaries**, rather than the entire 500,000-token document.

---

# 14. But There Is a Catch

Map-Reduce doesn't mean you can ignore context limits completely.

Imagine:

```text
100 chunks
     ↓
100 summaries
     ↓
Combine all summaries
     ↓
Reduce LLM
```

If the summaries are still huge, the Reduce step can exceed the context window.

For example:

```text
100 summaries × 1,000 tokens
             ↓
        100,000 tokens
```

You could still have a problem.

That's why production systems may use **hierarchical reduction**:

```text
Chunk 1 ─┐
Chunk 2 ─┤ → Summary A
Chunk 3 ─┤
Chunk 4 ─┘

Chunk 5 ─┐
Chunk 6 ─┤ → Summary B
Chunk 7 ─┤
Chunk 8 ─┘

Summary A ─┐
Summary B ─┤ → Final Summary
Summary C ─┘
```

This is essentially **recursive / hierarchical Map-Reduce**.

---

# 15. Parallelism

Another major advantage of Map-Reduce is that the Map operations are **independent**.

Instead of:

```text
Chunk 1 → LLM
          ↓
Chunk 2 → LLM
          ↓
Chunk 3 → LLM
```

you can conceptually process:

```text
Chunk 1 → LLM ─┐
Chunk 2 → LLM ─┤
Chunk 3 → LLM ─┤ → Reduce
Chunk 4 → LLM ─┘
```

This makes the Map stage suitable for parallel execution.

However, parallel calls increase API concurrency and can hit rate limits, so production implementations need appropriate concurrency control.

---

# 16. Map-Reduce vs Refine

### Map-Reduce

```text
Chunk 1 → Summary 1 ─┐
Chunk 2 → Summary 2 ─┤
Chunk 3 → Summary 3 ─┤
Chunk 4 → Summary 4 ─┘
                     ↓
                    LLM
                     ↓
               Final Summary
```

Independent processing.

### Refine

```text
Chunk 1 → Summary
            ↓
         + Chunk 2
            ↓
      Refined Summary
            ↓
         + Chunk 3
            ↓
      Refined Summary
```

Sequential processing.

### Key difference

**Map-Reduce:**

> "Summarize everything independently, then combine."

**Refine:**

> "Keep improving the existing summary as I read more."

---

# 17. Real-World Example: PDF Summarizer

Imagine you're building:

**AI Research Paper Summarizer**

```text
                 PDF
                  ↓
              PyPDFLoader
                  ↓
            50 pages
                  ↓
       RecursiveCharacterSplitter
                  ↓
             100 chunks
                  ↓
        ┌─────────┴─────────┐
        │                   │
      MAP                  MAP
        │                   │
      Chunk               Chunk
        ↓                   ↓
       LLM                 LLM
        ↓                   ↓
    Summary              Summary
        └─────────┬─────────┘
                  ↓
                REDUCE
                  ↓
                 LLM
                  ↓
          Research Summary
```

This is a very common architecture for long-document summarization.

---

# 18. When Should You Use Map-Reduce?

Use it when:

* The document is large.
* The entire document cannot fit into one prompt.
* You want independent processing of chunks.
* You want to potentially parallelize chunk processing.
* You need scalable long-document summarization.

Use **Stuff** when:

* The document is relatively small.
* Everything fits comfortably into the model context.
* You want the simplest implementation.
* You want fewer LLM calls.

---

## Final Mental Model

Remember these three words:

```text
MAP
 ↓
Summarize each chunk

REDUCE
 ↓
Combine chunk summaries

FINAL
 ↓
One coherent summary
```

So the complete formula is:

**Large Document → Split → Map → Intermediate Summaries → Reduce → Final Summary**

And compared with Stuff:

**Stuff = everything → one LLM call**

**Map-Reduce = chunks → many LLM calls → one final LLM call**

This is one of the most important **LangChain document-processing patterns** to understand before moving into RAG and production-grade document AI.
