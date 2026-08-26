# Set environment variable GOOGLE_API_KEY to Google key.

from langchain.chat_models import init_chat_model
from langchain.messages import SystemMessage, HumanMessage

model = init_chat_model("gemini-3.1-flash-lite", model_provider="google_genai")

messages = [SystemMessage(content="Give one line answer")]

while True:
    prompt = input("Enter prompt [q to quit, c to create new chat] :")
    if prompt.lower() == 'q':
        break
    # You can create HumanMessage or a dict with role user
    # messages.append( {"role" : "user", "content" : prompt})
    messages.append(HumanMessage(content=prompt))
    response = model.invoke(messages)
    print(response.content)
    print(f'Total Tokens : {response.usage_metadata["total_tokens"]}')
   
    
    # You can create AIMessage or a dict with role assistant
    # messages.append( {"role" : "assistant", "content" : response.content})
    messages.append(response) # AIMessage
