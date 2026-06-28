import os

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

embedding_model = HuggingFaceEmbeddings(
    model_name=MODEL_NAME
)

VECTOR_DB_PATH = "vector_store/faiss_index"


def create_vector_store(chunks):
    """
    Create FAISS vector database.
    """

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embedding_model
    )

    return vector_store


def save_vector_store(vector_store):
    """
    Save FAISS index locally.
    """

    vector_store.save_local(VECTOR_DB_PATH)

    print(" Vector Store Saved")


def load_vector_store():
    """
    Load FAISS index.
    """

    if not os.path.exists(VECTOR_DB_PATH):
        return None

    vector_store = FAISS.load_local(
        VECTOR_DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    print("Vector Store Loaded")

    return vector_store