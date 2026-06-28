"""
initialize.py

Initializes the complete Enterprise RAG system.

Responsibilities
----------------
1. Load PDF documents
2. Split documents into chunks
3. Create or Load FAISS Vector Store
4. Return a retriever for querying
"""

import os

from src.config import (
    DOCUMENTS_PATH,
    VECTOR_STORE_PATH,
)

from src.loaders.document_loader import load_all_documents
from src.processing.chunker import split_documents
from src.vectorstore.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store,
)


def initialize_rag():
    """
    Initialize the Enterprise RAG Knowledge Base.

    Returns
    -------
    FAISS Vector Store
    """

    print("=" * 60)
    print("Initializing Enterprise RAG...")
    print("=" * 60)

    # Try loading existing vector store
    vector_store = load_vector_store()

    if vector_store is not None:

        print("Existing Vector Store Loaded.")

    else:

        print("No Vector Store Found.")
        print("Building Knowledge Base...")

        documents = load_all_documents(DOCUMENTS_PATH)
        print(f"Documents Loaded : {len(documents)}")

        chunks = split_documents(documents)
        print(f"Chunks Created : {len(chunks)}")

        vector_store = create_vector_store(chunks)

        save_vector_store(vector_store)

        print("Knowledge Base Created Successfully.")

    print("Vector Store Ready.")
    print("=" * 60)

    return vector_store