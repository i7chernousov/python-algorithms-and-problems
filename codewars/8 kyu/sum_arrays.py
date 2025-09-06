"""
Write a function that takes an array of numbers and returns the sum of the numbers.
The numbers can be negative or non-integer.
If the array does not contain any numbers then you should return 0
"""

def sum_array(number_array: list) -> float | int:
    """Функция выполняет сумму чисел из входящего массива"""
    return sum(number_array)

if __name__ == "__main__":
    print(sum_array([]))
