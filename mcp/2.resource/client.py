import asyncio
from fastmcp import Client

client = Client("http://localhost:9999/mcp")

async def greet():
    async with client:
        # Call template resource 
        result = await client.read_resource(f"resource://greeting/Srikanth")
        print(result[0].text)

        # Call static resource 
        result = await client.read_resource(f"resource://today")
        print(result[0].text)

asyncio.run(greet())