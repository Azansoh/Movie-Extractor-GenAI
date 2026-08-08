from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage


model = ChatMistralAI(model="mistral-small-latest", temperature=0.7)


message=[SystemMessage(content="You are a funnay ai assistant.")]

print("----- Chatbot is ready! Type 'exit' or 'quit' to end the conversation. -----")
while True:
    user_input = input("User: ")
    message.append(HumanMessage(content=user_input))
    if user_input.lower() in ["exit", "quit"]:
        break

    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("AI:", response.content)


