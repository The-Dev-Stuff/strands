from strands import Agent
from strands_tools import calculator, current_time, python_repl

from agent_tools.text_tools import letter_counter
from llm_models.openai import openai_4_1

agent = Agent(
    model=openai_4_1,
    tools=[calculator, current_time, python_repl, letter_counter],
    callback_handler=None  # The default callback handler will print the agent's output to the console.
)

# This is an example of how to use the agent with multiple tools.
# Asking the agent to complete a few tasks, it will use the available tools.
# message = """
# I have 4 requests"
#
# 1. What is the time right now? Respond in the format "HH:MM:SS" (12-hour format), I'm in EST time zone by the way.
# 2. Calculate 3111696 / 74088
# 3. Tell me how many letter R's are in the word "strawberry" 🍓
# 4. Write a summary of what how you completed this task.
# """
# agent(message)
