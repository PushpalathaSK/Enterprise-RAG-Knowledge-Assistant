def build_prompt(question: str, documents):
    """
    Build a structured prompt using
    retrieved documents and the user's question.
    """

    context = "\n\n".join(
        [doc.page_content for doc in documents]
    )

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Use ONLY the information provided in the context.

If the answer is not available in the context, reply:

"I couldn't find this information in the provided documents."

Do not make up information.

--------------------------
Context:
{context}
--------------------------

Question:
{question}

Answer:
"""

    return prompt