# Module 5 – FAISS Vector Database

## Objective

Store embedding vectors efficiently and perform fast similarity search.

---

## What is FAISS?

FAISS (Facebook AI Similarity Search) is an open-source vector database developed by Meta.

It enables efficient searching among millions of vectors.

Instead of comparing every embedding one by one, FAISS builds an optimized index.

---

## Why Do We Need FAISS?

Without FAISS:

Question

↓

Compare with every embedding

↓

Slow

---

With FAISS:

Question

↓

Vector Search

↓

Top Similar Chunks

↓

Fast

---

## Workflow

Chunks

↓

Embeddings

↓

FAISS Index

↓

User Question

↓

Question Embedding

↓

Similarity Search

↓

Top Matching Chunks

---

## Advantages

- Extremely Fast
- Memory Efficient
- Supports Millions of Vectors
- Industry Standard

---

## FAISS in Our Project

Input:

Embedding vectors

Output:

Indexed vector database

---

## Next Module

Retriever

The retriever will use FAISS to fetch the most relevant chunks before sending them to Gemini.