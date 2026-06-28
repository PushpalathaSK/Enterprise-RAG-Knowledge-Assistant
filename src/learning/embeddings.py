from sentence_transformers import SentenceTransformer

# Load embedding model only once
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(chunks):
    """
    Generate embeddings for LangChain Document chunks.

    Returns
    -------
    embeddings : list
        List of embedding vectors
    """

    texts = [doc.page_content for doc in chunks]

    embeddings = embedding_model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings