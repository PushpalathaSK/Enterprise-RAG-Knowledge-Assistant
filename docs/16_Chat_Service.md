# Chat Service

## Objective

The Chat Service provides a single interface between the Streamlit UI and the Enterprise RAG Engine.

Instead of allowing the UI to communicate directly with document retrieval, prompt generation, and the language model, the Chat Service orchestrates the complete workflow.

## Responsibilities

- Receive the user's question
- Retrieve relevant documents
- Build the augmented prompt
- Generate the response using Gemini
- Return the answer and supporting source documents

## Workflow

User Question
      ↓
Retrieve Documents
      ↓
Prompt Builder
      ↓
Gemini
      ↓
Answer + Sources

## Benefits

- Separation of concerns
- Reusable backend logic
- Simplified UI
- Easier testing