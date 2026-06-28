from langchain_text_splitters import RecursiveCharacterTextSplitter
def split_documents(documents):
    """
    Split LangChain Document objects into smaller chunks.

    Parameters
    ----------
    documents : List[Document]

    Returns
    -------
    List[Document]
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    return chunks