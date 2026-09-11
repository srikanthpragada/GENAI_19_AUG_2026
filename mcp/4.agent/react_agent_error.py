# pip install langchain-mcp-adapters

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import asyncio

clients = MultiServerMCPClient(
    {"Math Server": {
        "url": "http://localhost:9999/mcp",
        "transport": "streamable_http"},
     "File Server:": {
        "url": "http://localhost:9000/mcp",
        "transport": "streamable_http"}
    }
)


async def process():
    tools = await clients.get_tools()
    model = init_chat_model("gemini-2.5-flash", model_provider="google-genai")
    agent = create_agent(model, tools)
    
    human_message = HumanMessage("Get contents of names.txt file")
    file_response = await agent.ainvoke({"messages": [human_message]})
   
    for msg in file_response['messages']:
        msg.pretty_print()


asyncio.run(process())
