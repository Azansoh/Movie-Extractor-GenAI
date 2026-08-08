from dotenv import load_dotenv
load_dotenv(override=True)





from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint




llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Flash-0731"
)
model = ChatHuggingFace(llm=llm)


response = model.invoke("give me a poem on ai?")
print(response.content)