"""
Задание № 1

Если выписать все натуральные числа меньше 10, кратные 3 или 5,
то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
"""

def sum_of_multiples(divisor_1: int, divisor_2: int, limit: int) -> int:
    """
    Функция вычисляет сумму всех натуральных чисел меньше limit,
    которые кратны divisor_1 или divisor_2

    :param divisor_1: Первый делитель
    :param divisor_2: Второй делитель
    :param limit: Максимальное число
    :return: Сумма кратных чисел
    """
    result = 0

    for number in range(1, limit):
        if number % divisor_1 == 0 or number % divisor_2 == 0:
            result += number

    return result


if __name__ == "__main__":
    print(sum_of_multiples(3, 5, 1000))
