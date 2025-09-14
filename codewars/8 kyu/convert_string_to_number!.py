"""
We need a function that can transform a string into a number.
What ways of achieving this do you know?
Note: Don't worry, all inputs will be strings,
and every string is a perfectly valid representation of an integral number.
"""


def string_to_number(string: str) -> int:
    """Функция конвертирует str в int"""
    return int(string)


if __name__ == "__main__":
    print(string_to_number("-7"))