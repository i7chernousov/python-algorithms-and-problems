"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
IPs should be considered valid if they consist of four octets,
with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89

Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
"""

def ip_validation(ip: str) -> bool:
    """ Проверка строки на валидацию формата IP адреса """
    octets = ip.split(".")

    # Проверка на формат IP с 4 значениями
    if len(octets) != 4:
        return False

    for i in octets:

        # Если значение не явлется цифрой
        if not i.isdigit():
            return False

        # Если в цифрах первый идет ноль
        if len(i) > 1 and i[0] == "0":
            return False

        # Если диапазон цисла не соответствует
        if not (int(i) >= 0 and int(i) <= 255):
            return False

    else:
        return True

if __name__ == '__main__':
    print(ip_validation("1.2.3.4.5"))

