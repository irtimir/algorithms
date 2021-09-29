"""
A. Полиномиальный хеш
Ограничение времени	0.5 секунд
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей написать функцию, вычисляющую хеш строки s.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:


Формат ввода
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому считается хеш.

Во второй строке дано число m (1 ≤ m ≤ 109) –— модуль.

В третьей строке дана строка s (0 ≤ |s| ≤ 106), состоящая из больших и маленьких латинских букв.

Формат вывода
Выведите целое неотрицательное число –— хеш заданной строки.
"""

import sys


def polynom_hash(s, q, R):
    res = 0

    for sym in s:
        res = (res * q + ord(sym)) % R

    return res


def main():
    q = int(sys.stdin.readline().rstrip())
    R = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()

    print(polynom_hash(s, q, R))


if __name__ == '__main__':
    main()