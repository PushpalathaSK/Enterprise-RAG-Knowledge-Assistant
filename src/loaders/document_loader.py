"""
Enterprise RAG Knowledge Assistant
----------------------------------
Document Loader Module

This module is responsible for loading PDF documents
and converting them into LangChain Document objects.
"""

import os

from langchain_community.document_loaders import PyPDFLoader

from src.config import DOCUMENTS_PATH


def load_single_pdf(file_path: str):
    """
    Load a single PDF document.

    Parameters
    ----------
    file_path : str
        Path to the PDF file.

    Returns
    -------
    list
        List of LangChain Document objects.
    """

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents


def load_all_documents(folder_path: str = DOCUMENTS_PATH):
    """
    Load all PDF documents from a folder.

    Parameters
    ----------
    folder_path : str
        Folder containing PDF files.

    Returns
    -------
    list
        Combined list of LangChain Document objects.
    """

    all_documents = []

    for file in sorted(os.listdir(folder_path)):

        if file.lower().endswith(".pdf"):

            print(f"Loading: {file}")

            file_path = os.path.join(folder_path, file)

            documents = load_single_pdf(file_path)

            all_documents.extend(documents)

    return all_documents