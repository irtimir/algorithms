"""
D. Кружки
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В компании, где работает Тимофей, заботятся о досуге сотрудников и устраивают различные кружки по интересам.
Когда кто-то записывается на занятие, в лог вносится название кружка.

По записям в логе составьте список всех кружков, в которые ходит хотя бы один человек.

Формат ввода
В первой строке даётся натуральное число n, не превосходящее 10 000 –— количество записей в логе.

В следующих n строках —– названия кружков.

Формат вывода
Выведите уникальные названия кружков по одному на строке, в порядке появления во входных данных.
"""

import sys


def main():
    n = int(sys.stdin.readline().rstrip())

    sections = []

    for _ in range(n):
        section = sys.stdin.readline().rstrip()
        if section not in sections:
            print(section)
            sections.append(section)


if __name__ == '__main__':
    main()