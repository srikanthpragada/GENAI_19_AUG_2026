# Program to create an Agent that chats with user and also has access to web using Tavily
# set TAVILY_API_KEY environment variable to Tavily API Key
# set GOOGLE_API_KEY environment variable to your Google API Key

from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

# Create the agent
memory = InMemorySaver()
model = init_chat_model("gemini-3.1-flash-lite", model_provider="google_genai")
search = TavilySearch(max_results=2)
tools = [search]

system_prompt = "Use tools only when necesary otherwise use you knowledge. Give answers as short as possible"
agent = create_agent(model, tools, system_prompt=system_prompt, checkpointer=memory)

thread_id = 1

# thread is identifies the session 
config = {"configurable": {"thread_id": thread_id}}

while True:
    prompt = input("Enter your prompt [q to quit, c to start new chat]:")
    if prompt.lower() == 'q':
        print('Thank you for chatting with me!!!')
        break

    if prompt.lower() == 'c':
        thread_id += 1
        config = {"configurable": {"thread_id": thread_id}}
        print("Starting a new chat.....")
        continue 

    human_message = HumanMessage(prompt)
    response = agent.invoke({"messages": [human_message]}, config=config)
 
    # display the result
    print("AI Response: ", response['messages'][-1].content)
 