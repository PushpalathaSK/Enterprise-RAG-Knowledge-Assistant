from src.llm import ask_gemini

question = "Explain Retrieval Augmented Generation in 5 lines."

answer = ask_gemini(question)

print(answer)