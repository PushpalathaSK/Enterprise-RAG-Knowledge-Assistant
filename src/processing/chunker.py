"""
Enterprise RAG Knowledge Assistant
----------------------------------
Document Chunking Module

This module splits LangChain Document objects into
smaller overlapping chunks for efficient semantic search.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


def split_documents(documents):
    """
    Split LangChain Document objects into smaller chunks.

    Parameters
    ----------
    documents : list
        List of LangChain Document objects.

    Returns
    -------
    list
        List of chunked LangChain Document objects.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=[
            "\n\n",
            "\n",
            ".",
            " ",
            "",
        ],
    )

    chunks = text_splitter.split_documents(documents)

    return chunks