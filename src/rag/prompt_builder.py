"""
Enterprise RAG Knowledge Assistant
----------------------------------
Prompt Builder Module

Creates structured prompts for the Gemini model.
"""


def build_prompt(
    *,
    question: str,
    documents,
):
    """
    Build a prompt using the retrieved documents.

    Parameters
    ----------
    question : str
        User question.

    documents : list
        Retrieved LangChain Document objects.

    Returns
    -------
    str
        Prompt sent to the LLM.
    """

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
You are an Enterprise Knowledge Assistant.

Instructions:
- Answer ONLY using the provided context.
- Do NOT make assumptions.
- If the answer is unavailable, reply:
  "I couldn't find this information in the uploaded documents."
- Keep answers clear and concise.
- Use bullet points when appropriate.

Context
-------
{context}

Question
--------
{question}

Answer
------
"""

    return prompt