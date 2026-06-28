# Module 4 – Embeddings

## Objective

The purpose of this module is to convert text chunks into numerical vector representations called **embeddings**.

These vectors capture the semantic meaning of the text and allow the system to perform **semantic similarity search** instead of simple keyword matching.

---

# Why Do We Need Embeddings?

Large Language Models (LLMs) cannot efficiently search through thousands of documents.

Instead, documents are converted into vectors.

When a user asks a question, the question is also converted into a vector.

The system then compares vectors instead of comparing words.

This enables the system to retrieve information based on **meaning** rather than exact keywords.

---

# Traditional Search vs Semantic Search

## Traditional Keyword Search

Query:

```
Vacation Policy
```

Document:

```
Leave Policy
```

Result:

❌ No Match (Different Words)

---

## Semantic Search

Query:

```
Vacation Policy
```

Document:

```
Leave Policy
```

Result:

✅ Match (Similar Meaning)

---

# What is an Embedding?

An embedding is a numerical representation of text.

Example:

Text:

```
Employees are entitled to 12 casual leaves.
```

Embedding:

```
[-0.024,
 0.131,
 -0.552,
 ...
 384 values]
```

The embedding itself has no human-readable meaning.

Instead, similar texts produce similar vectors.

---

# Embedding Workflow

```
Document

↓

Chunk

↓

Sentence Transformer

↓

Embedding Vector

↓

Vector Database (FAISS)
```

---

# Embedding Model Used

Model:

```
all-MiniLM-L6-v2
```

Reason:

- Free
- Lightweight
- Fast
- High-quality embeddings
- Runs locally
- Suitable for learning and production prototypes

---

# Why Not Use Gemini for Embeddings?

Google provides embedding models.

However, for this training project we use Sentence Transformers because:

- No API cost
- Faster development
- Runs offline
- Easier to understand
- Widely used in RAG tutorials and prototypes

---

# Embedding Dimensions

The model generates vectors of:

```
384 Dimensions
```

Each dimension represents learned semantic information.

Higher-dimensional vectors allow the model to capture richer relationships between texts.

---

# Project Flow

```
PDF

↓

Document Loader

↓

Chunks

↓

Embeddings

↓

FAISS

↓

Retriever

↓

Gemini

↓

Answer
```

---

# Input

List of LangChain Document objects.

Example:

```
Document(
    page_content="Employees are entitled to...",
    metadata={...}
)
```

---

# Output

List of embedding vectors.

Example:

```
[
 [-0.024, 0.132, ...],
 [ 0.551,-0.873, ...],
 ...
]
```

---

# Advantages

- Semantic understanding
- Fast similarity search
- Supports large document collections
- Reduces irrelevant retrieval
- Improves RAG answer quality

---

# Limitations

- Embeddings require additional storage.
- Better embedding models consume more memory.
- Embeddings must be regenerated when documents change.

---

# Module Summary

This module converts document chunks into dense vector representations.

These vectors form the foundation of semantic search and Retrieval-Augmented Generation (RAG).

The generated embeddings will be stored in a vector database during the next module.

---

# Next Module

Module 5 – FAISS Vector Database

In the next module, the generated embeddings will be indexed inside FAISS to enable fast semantic retrieval of relevant document chunks.