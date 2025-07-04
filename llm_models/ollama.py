import os
from dotenv import load_dotenv
from strands.models.ollama import OllamaModel

load_dotenv()

ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

ollama_llama = OllamaModel(
    host=ollama_host,
    model_id="llama3.2:latest"
)

ollama_qwen = OllamaModel(
    host=ollama_host,
    model_id="qwen3:8b"
)