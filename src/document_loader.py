import os
from langchain_community.document_loaders import PyPDFLoader


def load_single_pdf(file_path: str):
    """
    Load a single PDF and return a list of LangChain Document objects.
    """
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


def load_all_documents(folder_path: str):
    """
    Load all PDF files from a folder.
    Returns a combined list of Document objects.
    """
    all_documents = []

    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)

            print(f"Loading: {file}")

            loader = PyPDFLoader(file_path)
            documents = loader.load()

            all_documents.extend(documents)

    return all_documents