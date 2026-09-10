# set GOOGLE_API_KEY environment variable to your Google API Key

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
import json 


@tool()
def search_product(name : str) -> list[dict]:
    """Provide information about products with the given name

    Args:
        name : str
    """
    with open("products.json", "rt") as f:
         products = json.load(f) # list of dict
    
    # search
    selected_products = []
    for product in products:
         if name.lower() in product['name'].lower():
              selected_products.append(product)

    return selected_products


@tool()
def search_customer(name: str) -> list[dict]:
    """Provide information about customers with the given name

    Args:
        name : str
    """
    with open("customers.json", "rt") as f:
        customers = json.load(f)  # list of dict

    # search
    selected_customers = []
    for cust in customers:
        if name.lower() in cust['name'].lower():
            selected_customers.append(cust)

    return selected_customers


# Create the agent with tools
model = init_chat_model("gemini-3.1-flash-lite", model_provider="google_genai")
tools = [search_product, search_customer]

agent = create_agent(model, tools, system_prompt='Give minimum details')

#human_message = HumanMessage("Show me price of all mouse products")
human_message = HumanMessage("Give me email address of customer Rohit")
# Invoke agent
response = agent.invoke({"messages": [human_message]})

for message in response['messages']:
    message.pretty_print()
