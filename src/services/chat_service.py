"""
Enterprise RAG Knowledge Assistant
----------------------------------
Chat Service

Acts as the bridge between the Streamlit UI and the RAG Engine.
"""

from src.rag.initialize import initialize_rag
from src.rag.retriever import retrieve_documents
from src.rag.prompt_builder import build_prompt
from src.llm.llm import ask_gemini


class ChatService:
    """
    Enterprise RAG Chat Service
    """

    def __init__(self):
        """
        Initialize the Enterprise RAG system.
        """

        self.vector_store = initialize_rag()

    def ask_question(self, question: str):
        """
        Process a user question.

        Parameters
        ----------
        question : str
            User question.

        Returns
        -------
        tuple
            (answer, source_documents)
        """

        # ----------------------------------------
        # Retrieve Relevant Documents
        # ----------------------------------------

        documents = retrieve_documents(
            vector_store=self.vector_store,
            question=question,
        )

        # ----------------------------------------
        # Build Prompt
        # ----------------------------------------

        prompt = build_prompt(
            question=question,
            documents=documents,
        )

        # ----------------------------------------
        # Generate Answer
        # ----------------------------------------

        answer = ask_gemini(prompt)

        # ----------------------------------------
        # Return Result
        # ----------------------------------------

        return answer, documents