"""
Very simple, given a number (integer / decimal / both depending on the language),
find its opposite (additive inverse).
"""

def opposite(number: float) -> float:
    """Функция возвращает аддитивную противоположность числа (меняет знак)"""
    return -number


if __name__ == "__main__":
    print(opposite(1))