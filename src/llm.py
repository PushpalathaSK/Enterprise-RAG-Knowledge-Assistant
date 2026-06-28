import google.generativeai as genai
from src.config import GOOGLE_API_KEY, MODEL_NAME

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


def ask_gemini(question: str):
    response = model.generate_content(question)
    return response.text