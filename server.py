from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from agent_definition import agent, local_agent
from mcp_tooling.mcp_servers import my_mcp_server
import logging

app = FastAPI()

# Enable debug logging for Strands / Remove this in production
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)


class PromptRequest(BaseModel):
    prompt: str


@app.post("/chat")
async def stream_response(request: PromptRequest):
    """
    Endpoint to handle chat requests and stream responses.
    """
    prompt = request.prompt
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    # Simulate a streaming response
    async def generate_response():
        try:
            # Use with the MCP client context manager to ensure proper cleanup
            with my_mcp_server:
                mcp_tools = my_mcp_server.list_tools_sync()
                agent.tool_registry.process_tools(mcp_tools)

                print(f"Available tools for openai agent: {[tool.tool_name for tool in mcp_tools]}")

                async for event in agent.stream_async(request.prompt):
                    if "data" in event:
                        # Only stream text chunks to client
                        yield event["data"]
        except Exception as e:
            yield f"Error occurred: {str(e)}\n"

    return StreamingResponse(generate_response(), media_type="text/plain")


@app.post("/chat-local")
async def stream_response(request: PromptRequest):
    """
    Endpoint to handle chat requests and stream responses.
    """
    prompt = request.prompt
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty.")

    # Simulate a streaming response
    async def generate_response():
        try:
            # Use with the MCP client context manager to ensure proper cleanup
            with my_mcp_server:
                mcp_tools = my_mcp_server.list_tools_sync()
                local_agent.tool_registry.process_tools(mcp_tools)

                print(f"Available tools for local agent: {[tool.tool_name for tool in mcp_tools]}")

                async for event in local_agent.stream_async(request.prompt):
                    if "data" in event:
                        # Only stream text chunks to client
                        yield event["data"]
        except Exception as e:
            yield f"Error occurred: {str(e)}\n"

    return StreamingResponse(generate_response(), media_type="text/plain")
