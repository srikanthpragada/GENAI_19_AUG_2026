from langchain.messages import SystemMessage, HumanMessage
from langchain_ollama import ChatOllama
 
model = ChatOllama(model="llama3.2:latest")
messages = [SystemMessage(content="Give one line answer")]

while True:
    prompt = input("Enter prompt [q to quit, c to create new chat] :")
    if prompt.lower() == 'q':
        break

    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    print(response.content)
    
    messages.append(response) # AIMessage
