"""
C. DFS
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	1 секунда	256Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	2 секунды	256Mb
Python 3.7.3	2 секунды	128Mb
Oracle Java 8	2 секунды	256Mb
OpenJDK Java 11	2 секунды	256Mb
Node JS 8.16	2 секунды	256Mb
Задан неориентированный граф. Обойдите с помощью DFS все вершины, достижимые из заданной вершины s, и выведите их в
порядке обхода, если начинать обход из s.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой вершины s
(1 ≤ s ≤ n). В графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться
в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
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


def dfs(start_vertex, adjacency):
    stack = Stack()
    stack.push(start_vertex)
    colors = [WHITE] * len(adjacency)

    while stack.size():
        v = stack.pop()
        if colors[v - 1] == WHITE:
            yield v
            colors[v - 1] = GRAY
            stack.push(v)

            for w in sorted(adjacency[v], reverse=True):
                if colors[w - 1] == WHITE:
                    stack.push(w)

        elif colors[v - 1] == GRAY:
            colors[v - 1] = BLACK


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adjacency = {v: [] for v in range(1, n + 1)}

    for _ in range(m):
        f, t = map(int, sys.stdin.readline().rstrip().split())
        adjacency[f].append(t)
        adjacency[t].append(f)

    s = int(sys.stdin.readline().rstrip())

    print(*dfs(s, adjacency))


if __name__ == '__main__':
    main()
