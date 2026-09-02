from langchain_ollama import ChatOllama
 
llm = ChatOllama(model="llama3.2:latest")
response = llm.invoke("When did world war 1 start?")
print(response.content)
 
