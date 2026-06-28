from src.rag.initialize import initialize_rag

vector_store = initialize_rag()

print("\nEnterprise RAG Initialized Successfully")

print(type(vector_store))