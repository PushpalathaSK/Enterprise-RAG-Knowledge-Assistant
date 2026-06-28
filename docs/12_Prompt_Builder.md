# Module 6 – Prompt Builder

## Objective

Construct a structured prompt for the Large Language Model using:

- Retrieved Context
- User Question
- System Instructions

---

## Why Do We Need Prompt Engineering?

The Large Language Model performs better when it receives structured instructions.

Instead of sending only the retrieved chunks, we provide:

- Role
- Context
- Rules
- User Question

---

## Prompt Structure

System Instructions

↓

Retrieved Context

↓

User Question

↓

LLM

↓

Answer

---

## Rules

- Answer only from the provided context.
- Do not hallucinate.
- If the answer is unavailable, clearly say so.
- Mention the source when possible.

---

## Output

A formatted prompt ready to be sent to Gemini.

---

## Next Module

RAG Pipeline