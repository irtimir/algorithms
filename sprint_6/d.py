"""
D. BFS
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.7 секунд	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	2.1 секунда	256Mb
Python 3.7.3	1.5 секунд	64Mb
Mono C# 5.2.0	1.5 секунд	256Mb
Oracle Java 8	1.5 секунд	256Mb
OpenJDK Java 11	1.5 секунд	256Mb
Node JS 8.16	2.1 секунда	256Mb
Задан неориентированный связный граф. Обойдите его поиском в ширину, стартуя из заданной вершины, и выведите вершины в
порядке обхода.

Формат ввода
В первой строке дано количество вершин n (1 ≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 105). Далее в m строках описаны рёбра графа.
Каждое ребро описывается номерами двух вершин u и v (1 ≤ u, v ≤ n). В последней строке дан номер стартовой
вершины s (1 ≤ s ≤ n).

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите вершины в порядке обхода, считая что при запуске от каждой конкретной вершины её соседи будут рассматриваться
в порядке возрастания (то есть если вершина 2 соединена с 1 и 3, то сначала обход пойдёт в 1, а уже потом в 3).
"""

import sys


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self):
        if self.head:
            elem = self.head.value
            self.head = self.head.next_item
            self.size -= 1
            if self.head is None:
                self.tail = None

            return elem

    def put(self, value):
        n = Node(value)
        if self.tail:
            self.tail.next_item = n
        else:
            self.head = n
        self.tail = n
        self.size += 1


WHITE = 0
GRAY = 1
BLACK = 2


def bfs(start, adjacency):
    color = [WHITE] * (len(adjacency) + 1)
    previous = [None] * (len(adjacency) + 1)
    distance = [0] * (len(adjacency) + 1)

    planned = Queue()
    planned.put(start)
    color[start] = GRAY
    distance[start] = 0

    while planned.size:
        u = planned.get()

        yield u

        for v in sorted(adjacency[u]):
            if color[v] == WHITE:
                distance[v] = distance[u] + 1
                previous[v] = u
                color[v] = GRAY
                planned.put(v)

        color[u] = BLACK


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adjacency = {v: [] for v in range(1, n + 1)}

    for _ in range(m):
        f, t = map(int, sys.stdin.readline().rstrip().split())
        adjacency[f].append(t)
        adjacency[t].append(f)

    start = int(sys.stdin.readline().rstrip())

    print(*bfs(start, adjacency))


if __name__ == '__main__':
    main()
