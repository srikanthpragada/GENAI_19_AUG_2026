# Set environment variable - HUGGINGFACE_HUB_TOKEN - to access token

from langchain_huggingface import (
    HuggingFaceEndpoint,
    ChatHuggingFace,
)

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b")

chat = ChatHuggingFace(llm=llm)

response = chat.invoke("Which is the capital of Sweden?")
print(response.content)
