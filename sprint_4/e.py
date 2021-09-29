"""
E. Подстроки
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.077 секунд	4Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	0.1 секунда	64Mb
Oracle Java 8	0.1 секунда	64Mb
OpenJDK Java 11	0.3 секунды	64Mb
Node JS 8.16	0.1 секунда	64Mb
На вход подается строка. Нужно определить длину наибольшей подстроки, которая не содержит повторяющиеся символы.

Формат ввода
Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит 10 000.

Формат вывода
Выведите натуральное число —– ответ на задачу.
"""

# abcabcbb
# 3

# bbbbb
# 1

import sys


def main():
    symbols = sys.stdin.readline().rstrip()

    if len(symbols) == 1:
        print(1)
        return

    max_l = 0
    start_idx = 0

    while True:
        prev_elements = set()
        if start_idx == len(symbols) - 1:
            break
        for i in range(start_idx, len(symbols)):
            if symbols[i] not in prev_elements:
                prev_elements.add(symbols[i])
            else:
                start_idx += 1
                max_c = len(prev_elements)
                if max_l < max_c:
                    max_l = max_c
                break
        else:
            max_c = len(prev_elements)
            if max_l < max_c:
                max_l = max_c
            break

    print(max_l)


if __name__ == '__main__':
    main()
