from src.loaders.document_loader import load_all_documents
from src.processing.chunker import split_documents

folder = "data/documents"

documents = load_all_documents(folder)

print(f"\nDocuments Loaded : {len(documents)}")

chunks = split_documents(documents)

print(f"Chunks Created : {len(chunks)}")

print("\n----------------------------------")
print("FIRST CHUNK")
print("----------------------------------")

print(chunks[0].page_content)

print("\nMetadata")
print(chunks[0].metadata)