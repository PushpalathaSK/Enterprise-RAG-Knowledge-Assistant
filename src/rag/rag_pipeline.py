from src.rag.retriever import retrieve_documents
from src.rag.prompt_builder import build_prompt
from src.llm.llm import ask_gemini


def ask_question(question, vector_store):
    """
    Complete RAG Pipeline

    Question
        ↓
    Retriever
        ↓
    Prompt Builder
        ↓
    Gemini
        ↓
    Answer
    """

    retrieved_docs = retrieve_documents(
        vector_store=vector_store,
        question=question,
        k=3
    )

    prompt = build_prompt(
        question,
        retrieved_docs
    )

    answer = ask_gemini(prompt)

    return answer, retrieved_docs