"""
Enterprise RAG Knowledge Assistant
----------------------------------
LLM Module

This module is responsible for communicating
with Google's Gemini model.
"""

import google.generativeai as genai

from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
)

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Load Gemini Model
model = genai.GenerativeModel(LLM_MODEL)


def ask_gemini(prompt: str):
    """
    Send a prompt to Gemini and return the generated response.

    Parameters
    ----------
    prompt : str
        Prompt sent to the Gemini model.

    Returns
    -------
    str
        Generated response text.
    """

    response = model.generate_content(prompt)

    return response.text