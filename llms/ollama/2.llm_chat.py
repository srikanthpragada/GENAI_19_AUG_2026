from langchain_ollama import ChatOllama
 
llm = ChatOllama(model="llama3.2:latest")
response = llm.invoke("Who is Guido Van Rossum?")
print(response.content)
 
