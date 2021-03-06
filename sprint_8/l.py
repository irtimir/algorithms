"""
L. Подсчёт префикс-функции
Все языки	Python 3.7.3	GNU c++17 7.3
Ограничение времени	1 секунда	1.6 секунд	0.4 секунды
Ограничение памяти	128Mb	128Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В этой задаче вам необходимо посчитать префикс-функцию для заданной строки.

Формат ввода
На вход подаётся строка, состоящая из строчных латинских букв. Длина строки не превосходит 106.

Формат вывода
Если длина входной строки L, то выведите через пробел L целых неотрицательных чисел —– массив значений префикс-функции
исходной строки.
"""

import sys


def prefix_func(s):
    pi = [-1 for _ in range(len(s))]
    pi[0] = 0

    for i in range(1, len(s)):
        k = pi[i - 1]
        while k > 0 and s[k] != s[i]:
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1

        pi[i] = k

    return pi


def main():
    s = sys.stdin.readline().rstrip()

    print(' '.join(map(str, prefix_func(s))))


if __name__ == '__main__':
    main()
