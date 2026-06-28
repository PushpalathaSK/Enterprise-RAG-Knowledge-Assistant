from src.loaders.document_loader import load_all_documents
from src.processing.chunker import split_documents
from src.vectorstore.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store,
)

documents = load_all_documents("data/documents")

chunks = split_documents(documents)

vector_db = create_vector_store(chunks)

save_vector_store(vector_db)

loaded_db = load_vector_store()

print()

print("Total vectors")

print(loaded_db.index.ntotal)