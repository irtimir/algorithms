"""
I. Разные деревья поиска
Все языки	Oracle Java 8	OpenJDK Java 11
Ограничение времени	1 секунда	0.3 секунды	0.3 секунды
Ограничение памяти	64Mb	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Ребятам стало интересно, сколько может быть различных деревьев поиска, содержащих в своих узлах все уникальные числа
от 1 до n. Помогите им найти ответ на этот вопрос.

Формат ввода
В единственной строке задано число n. Оно не превосходит 20.

Формат вывода
Нужно вывести число, равное количеству различных деревьев поиска, в узлах которых могут быть размещены числа от 1 до n
включительно.
"""

import sys


def tree_count(n):
    if n >= 2:
        c = ((2 * ((2 * n) - 1)) / (n + 1)) * tree_count(n - 1)
        return int(c)
    return 1


def main():
    n = int(sys.stdin.readline().rstrip())

    print(tree_count(n))


if __name__ == '__main__':
    main()
