from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_mistralai import ChatMistralAI

# Option A: Using prefix
model = ChatMistralAI(model="mistral-small-latest")

# Option B: Using model_provider parameter
# model = ChatMistralAI(model="llama-3.3-70b-versatile", model_provider="groq")

response = model.invoke("give me a paragraph on machine learning?")

print(response.content)