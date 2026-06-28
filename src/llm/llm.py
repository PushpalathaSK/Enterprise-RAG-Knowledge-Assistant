import google.generativeai as genai

from src.config import (
    GEMINI_API_KEY,
    LLM_MODEL,
)

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(LLM_MODEL)


def ask_gemini(prompt: str):

    response = model.generate_content(prompt)

    return response.text