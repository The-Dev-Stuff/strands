import os

from dotenv import load_dotenv
from strands.models.openai import OpenAIModel

load_dotenv()

openai_4_1 = OpenAIModel(
    client_args={
        "api_key": os.environ.get("OPENAI_KEY")
    },
    model_id="gpt-4.1",
)
