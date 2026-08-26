from langchain_ollama import ChatOllama

model = ChatOllama(model="gemma3:1b")
prompt = """Find the sentiment in the text below. Just give only sentiment without any details:
Text: I hate your website as it doesn't show any userful information.
Sentiment: 
"""
result = model.invoke(prompt) 
print(result.content)
