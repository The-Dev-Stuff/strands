from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from agent_definition import agent

app = FastAPI()


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
            async for event in agent.stream_async(request.prompt):
                if "data" in event:
                    # Only stream text chunks to client
                    yield event["data"]
        except Exception as e:
            yield f"Error occurred: {str(e)}\n"

    return StreamingResponse(generate_response(), media_type="text/plain")
