from strands import tool

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
