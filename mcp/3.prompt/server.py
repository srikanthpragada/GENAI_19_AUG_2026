from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Prompt Server")

# Prompt returning a specific message type
@mcp.prompt
def code_request(language: str, task: str) -> str:
    """Generates a user message requesting code generation."""
    content = f"Write a {language} function that performs the following task: {task}"
    return content 

 
mcp.run(transport="http", port=9999)