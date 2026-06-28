from src.document_loader import load_all_documents

folder = "data/documents"

documents = load_all_documents(folder)

print("\n--------------------------------")
print(f"Total Pages Loaded : {len(documents)}")
print("--------------------------------\n")

print("First Document Metadata:")
print(documents[0].metadata)

print("\n--------------------------------\n")

print("First 500 Characters:\n")
print(documents[0].page_content[:500])