from src.loaders.document_loader import load_all_documents
from src.processing.chunker import split_documents
from src.vectorstore.vector_store import create_vector_store
from src.rag.rag_pipeline import ask_question

documents = load_all_documents("data/documents")

chunks = split_documents(documents)

vector_db = create_vector_store(chunks)

question = "How many casual leaves are allowed?"

answer, docs = ask_question(
    question,
    vector_db
)

print("=" * 80)
print("QUESTION")
print(question)

print("\n" + "=" * 80)
print("ANSWER")
print(answer)

print("\n" + "=" * 80)
print("SOURCES")

for doc in docs:
    print(doc.metadata["source"])