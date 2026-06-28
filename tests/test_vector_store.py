from src.loaders.document_loader import load_all_documents
from src.processing.chunker import split_documents
from src.vectorstore.vector_store import create_vector_store

documents = load_all_documents("data/documents")

chunks = split_documents(documents)

vector_db = create_vector_store(chunks)

print("\nVector Store Created Successfully!")

print(f"\nTotal Chunks Indexed : {vector_db.index.ntotal}")