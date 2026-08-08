from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_huggingface import HuggingFaceEmbeddings

# Pass the model name directly
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector = embedding.embed_query("What is the capital of France?")

print("Vector length:", len(vector))
print("Sample vector values:", vector[:5])