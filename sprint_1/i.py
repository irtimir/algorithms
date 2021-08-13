"""
Вася на уроке математики изучил степени.
Теперь он хочет написать программу, которая определяет, будет ли положительное целое число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.
"""
import sys


def main():
    digit = int(sys.stdin.readline().rstrip())

    if digit == 1:
        print(True)
        return
    elif 1 < digit < 4 or digit % 2 != 0:
        print(False)
        return

    counter = 0
    last_digit = digit

    while last_digit >= 4:
        if last_digit % 4 != 0:
            print(False)
            return

        last_digit = last_digit / 4
        counter += 1

    if 4 ** counter == digit:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
