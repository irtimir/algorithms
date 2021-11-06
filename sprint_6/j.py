"""
J. Топологическая сортировка
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.3 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	0.7 секунд	128Mb
Python 3.7.3	1 секунда	64Mb
Oracle Java 8	0.7 секунд	128Mb
OpenJDK Java 11	0.7 секунд	128Mb
Node JS 8.16	0.7 секунд	128Mb
Дан ациклический ориентированный граф (так называемый DAG, directed acyclic graph). Найдите его топологическую
сортировку, то есть выведите его вершины в таком порядке, что все рёбра графа идут слева направо. У графа может быть
несколько подходящих перестановок вершин. Вам надо найти любую топологическую сортировку.

Формат ввода
В первой строке даны два числа – количество вершин n (1 ≤ n ≤ 105) и количество рёбер m (0 ≤ m ≤ 105). В каждой из
следующих m строк описаны рёбра по одному на строке. Каждое ребро представлено парой вершин (from, to),
1≤ from, to ≤ n, соответственно номерами вершин начала и конца.

Формат вывода
Выведите номера вершин в требуемом порядке.
"""

import sys

WHITE = 0
GRAY = 1
BLACK = 2


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def top_sort(start_vertex, adjacency, colors, stack_sort):
    stack = Stack()
    stack.push(start_vertex)

    while stack.size():
        v = stack.pop()
        if colors[v - 1] == WHITE:
            colors[v - 1] = GRAY
            stack.push(v)

            for w in sorted(adjacency[v], reverse=True):
                if colors[w - 1] == WHITE:
                    stack.push(w)

        elif colors[v - 1] == GRAY:
            colors[v - 1] = BLACK
            stack_sort.push(v)


def main_top_sort(adjacency):
    stack = Stack()
    colors = [WHITE] * len(adjacency)

    for i in range(1, len(adjacency) + 1):
        if colors[i - 1] == WHITE:
            top_sort(i, adjacency, colors, stack)

    while stack.size():
        yield stack.pop()


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adjacency = {v: [] for v in range(1, n + 1)}

    for _ in range(m):
        f, t = map(int, sys.stdin.readline().rstrip().split())
        adjacency[f].append(t)

    print(*main_top_sort(adjacency))


if __name__ == '__main__':
    main()
