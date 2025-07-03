from dotenv import load_dotenv
import os
from strands import Agent, tool
from strands.models.openai import OpenAIModel
from strands_tools import calculator, current_time, python_repl

load_dotenv()

# Defining a custom tool / a function the agent can use.
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count the occurrences of a specific letter in a given word.

    Args:
        word (str): The word to search within.
        letter (str): The letter to count in the word.

    Returns:
        int: The number of times the letter appears in the word.
    """
    if not isinstance(word, str) or not isinstance(letter, str):
        raise 0

    if len(letter) != 1:
        raise ValueError("The 'letter' must be a single character.")

    return word.lower().count(letter.lower())


# Creating an agent and giving it access to a few tools provided by Strands and the one we just created.
# Also defining which model to use.

model = OpenAIModel(
    client_args={
        "api_key": os.environ.get("OPENAI_KEY")
    },
    model_id="gpt-4.1",
)

agent = Agent(
    model=model,
    tools=[calculator, current_time, python_repl, letter_counter],
    callback_handler=None # The default callback handler will print the agent's output to the console.
)

# Asking the agent to complete a few tasks, it will use the available tools.
message = """
I have 4 requests"

1. What is the time right now? Respond in the format "HH:MM:SS" (12-hour format), I'm in EST time zone by the way.
2. Calculate 3111696 / 74088
3. Tell me how many letter R's are in the word "strawberry" 🍓
4. Write a summary of what how you completed this task.
"""
agent(message)