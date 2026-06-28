from src.loaders.document_loader import load_all_documents
from src.processing.chunker import split_documents
from src.vectorstore.vector_store import create_vector_store
from src.rag.retriever import retrieve_documents
from src.rag.prompt_builder import build_prompt

documents = load_all_documents("data/documents")

chunks = split_documents(documents)

vector_db = create_vector_store(chunks)

question = "How many casual leaves are allowed?"

results = retrieve_documents(
    vector_db,
    question,
    k=3
)

prompt = build_prompt(question, results)

print(prompt)