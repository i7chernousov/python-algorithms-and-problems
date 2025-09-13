"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
Names given are always valid strings.
"""


def are_you_playing_banjo(name: str) -> str:
    """Возвращает строку о том, играет ли человек на банджо."""

    if name.lower().startswith("r"):
        return f"{name} plays banjo"

    return f"{name} does not play banjo"




if __name__ == "__main__":
    print(are_you_playing_banjo("Martin"))
