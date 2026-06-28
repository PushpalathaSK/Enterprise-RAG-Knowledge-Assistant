from src.services.chat_service import ChatService


chat = ChatService()

question = "How many casual leaves are allowed?"

answer, sources = chat.ask_question(question)

print("\n")
print("=" * 80)
print("QUESTION")
print(question)

print("\n")
print("=" * 80)
print("ANSWER")
print(answer)

print("\n")
print("=" * 80)
print("SOURCES")

for doc in sources:
    print(doc.metadata["source"])