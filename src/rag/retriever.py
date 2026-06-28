from langchain_core.vectorstores import VectorStore


def retrieve_documents(
    vector_store: VectorStore,
    question: str,
    k: int = 3
):
    """
    Retrieve the top-k most relevant document chunks
    from the vector store.
    """

    results = vector_store.similarity_search(
        query=question,
        k=k
    )

    return results