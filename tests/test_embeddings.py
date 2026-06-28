from src.loaders.document_loader import load_all_documents
from src.processing.chunker import split_documents
from src.learning.embeddings import create_embeddings

documents = load_all_documents("data/documents")

chunks = split_documents(documents)

embeddings = create_embeddings(chunks)

print("\n--------------------------------")
print(f"Chunks : {len(chunks)}")
print(f"Embeddings : {len(embeddings)}")
print("--------------------------------")

print("\nDimension of first embedding:")

print(len(embeddings[0]))

print("\nFirst 10 values:\n")

print(embeddings[0][:10])