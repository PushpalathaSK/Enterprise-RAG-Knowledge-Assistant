# Module 5 – Retriever

## Objective

Retrieve the most relevant document chunks from the FAISS vector database based on a user's question.

---

## Why Do We Need a Retriever?

The vector database contains many document chunks.

Instead of sending every chunk to the Large Language Model (LLM), the retriever selects only the most relevant ones.

This reduces:

- Cost
- Latency
- Token usage

while improving answer quality.

---

## Workflow

User Question

↓

Embedding

↓

FAISS Similarity Search

↓

Top K Chunks

↓

LLM

↓

Answer

---

## Input

Question

Example:

"What is the leave policy?"

---

## Output

Top matching LangChain Document objects.

---

## Retrieval Strategy

Similarity Search

Top K = 3

---

## Advantages

- Faster response
- Better context
- Lower API cost
- Higher answer accuracy

---

## Next Module

RAG Pipeline