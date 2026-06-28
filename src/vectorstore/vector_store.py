import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from src.config import (
    EMBEDDING_MODEL,
    VECTOR_STORE_PATH,
)

embedding_model = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)


def create_vector_store(chunks):
    """
    Create FAISS vector database.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model,
    )

    return vector_store


def save_vector_store(vector_store):
    """
    Save FAISS index locally.
    """

    vector_store.save_local(VECTOR_STORE_PATH)

    print("✅ Vector Store Saved")


def load_vector_store():
    """
    Load FAISS index from disk.
    """

    if not os.path.exists(VECTOR_STORE_PATH):
        return None

    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embedding_model,
        allow_dangerous_deserialization=True,
    )

    print("✅ Vector Store Loaded")

    return vector_store