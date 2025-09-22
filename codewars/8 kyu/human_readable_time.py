"""
Write a function, which takes a non-negative integer (seconds)
as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""

def make_readable(number) -> str:
    """Функция преобразует количество секунд в формат HH:MM:SS"""
    hours = number // 3600
    minutes = (number - (hours * 3600)) // 60
    seconds = number - (hours * 3600 + minutes * 60)

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

if __name__ == '__main__':
    print(make_readable(60))
