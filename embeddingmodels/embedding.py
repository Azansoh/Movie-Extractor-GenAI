from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_openai import OpenAIEmbeddings

# Initialize OpenAI embeddings with custom dimensions
embedding = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)

vector = embedding.embed_query("What is the capital of France?")

print("Vector length:", len(vector))
print("Sample vector values:", vector[:5])