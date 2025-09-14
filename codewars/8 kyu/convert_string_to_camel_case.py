"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text: str) -> str:
    """Функция преобразовывает введенный текст в верблюжий регистр"""
    text = text.replace("-", "_").split("_")

    # Записываем первое слово в строку
    result = text[0]

    # Преобразовываем остальные слова с заглавной буквы
    for i in text[1:]:
        result += i.capitalize()

    return result


if __name__ == "__main__":
    print(to_camel_case("the-stealth-warrior"))