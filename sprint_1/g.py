"""
Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную.
Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.
Не используйте встроенные средства языка по переводу чисел в бинарное представление.
"""

import sys


def main():
    digit = int(sys.stdin.readline().rstrip())

    last_digit = digit
    res = []

    while last_digit != 1:
        res.append(str(last_digit % 2))
        last_digit = last_digit // 2

    res.append(str(1))
    res.reverse()

    print(''.join(res))


if __name__ == '__main__':
    main()
