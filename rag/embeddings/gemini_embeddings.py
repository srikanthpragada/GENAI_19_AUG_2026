from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

embeddings_model = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")

docs = [
    "AI is transforming the world.",
    "Machine learning enables data-driven predictions.",
    "Deep learning uses neural networks."
]

embeddings = embeddings_model.embed_documents(docs)
print(len(embeddings), len(embeddings[0]))
print(embeddings[0][:10])

