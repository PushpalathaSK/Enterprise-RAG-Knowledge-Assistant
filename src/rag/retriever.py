"""
Enterprise RAG Knowledge Assistant
----------------------------------
Retriever Module

Retrieves the most relevant document chunks
from the FAISS vector database.
"""

from langchain_core.vectorstores import VectorStore

from src.config import TOP_K


def retrieve_documents(
    vector_store: VectorStore,
    question: str,
    k: int = TOP_K,
):
    """
    Retrieve the top-k most relevant document chunks.

    Parameters
    ----------
    vector_store : VectorStore
        FAISS vector database.

    question : str
        User question.

    k : int
        Number of documents to retrieve.

    Returns
    -------
    list
        List of LangChain Document objects.
    """

    return vector_store.similarity_search(
        query=question,
        k=k,
    )