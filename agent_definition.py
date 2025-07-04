from strands import Agent
from strands_tools import calculator, current_time, python_repl

from agent_tools.text_tools import letter_counter
from llm_models.ollama import ollama_qwen
from llm_models.openai import openai_4_1

baseTools = [calculator, current_time, python_repl, letter_counter]

agent = Agent(
    model=openai_4_1,
    tools=baseTools,
    callback_handler=None  # The default callback handler will print the agent's output to the console.
)

local_agent = Agent(
    model=ollama_qwen,
    tools=baseTools,
    callback_handler=None  # The default callback handler will print the agent's output to the console.
)


