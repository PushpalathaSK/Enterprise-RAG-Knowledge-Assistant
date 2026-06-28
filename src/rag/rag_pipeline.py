"""
Enterprise RAG Knowledge Assistant
----------------------------------
RAG Pipeline Module
"""

from src.rag.prompt_builder import build_prompt
from src.rag.retriever import retrieve_documents
from src.llm.llm import ask_gemini


def ask_question(question, vector_store):
    """
    Execute the complete RAG pipeline.
    """

    documents = retrieve_documents(
        vector_store=vector_store,
        question=question,
    )

    prompt = build_prompt(
        question,
        documents,
    )

    answer = ask_gemini(prompt)

    return {
        "answer": answer,
        "documents": documents,
    }