import os

from dotenv import load_dotenv
from mcp.client.streamable_http import streamablehttp_client
from strands.tools.mcp import MCPClient

load_dotenv()

# Referencing a local MCP server running on port 3000.
my_mcp_server = MCPClient(
    lambda: streamablehttp_client(os.environ.get("MY_MCP_SERVER_URL", "http://localhost:3000/mcp")))
