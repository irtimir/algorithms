"""
E. Компоненты связности
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.5 секунд	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	1 секунда	128Mb
Python 3.7.3	1.5 секунд	64Mb
Oracle Java 8	1 секунда	128Mb
OpenJDK Java 11	1 секунда	128Mb
Node JS 8.16	1 секунда	128Mb
Вам дан неориентированный граф. Найдите его компоненты связности.

Формат ввода
В первой строке дано количество вершин n (1≤ n ≤ 105) и рёбер m (0 ≤ m ≤ 2 ⋅ 105). В каждой из следующих m строк
записано по ребру в виде пары вершин 1 ≤ u, v ≤ n.

Гарантируется, что в графе нет петель и кратных рёбер.

Формат вывода
Выведите все компоненты связности в следующем формате: в первой строке выведите общее количество компонент.

Затем на отдельных строках выведите вершины каждой компоненты, отсортированные по возрастанию номеров. Компоненты между
собой упорядочивайте по номеру первой вершины.
"""

import sys

WHITE = -1
GRAY = -2


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def dfs(start_vertex, adjacency, black_num):
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
            colors[v - 1] = black_num


def group_by_components(adjacency):
    colors = [-1] * len(adjacency)
    component_count = 0

    groups = []

    for i in range(1, len(colors) + 1):
        if colors[i - 1] == -1:
            group = []
            for v in dfs(i, adjacency, component_count):
                colors[v - 1] = component_count
                group.append(v)

            groups.append(group)
            component_count += 1

    return component_count, list(groups)


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adjacency = {v: [] for v in range(1, n + 1)}

    for _ in range(m):
        f, t = map(int, sys.stdin.readline().rstrip().split())
        adjacency[f].append(t)
        adjacency[t].append(f)

    componens_num, components = group_by_components(adjacency)

    print(componens_num)
    components.sort()

    for group in components:
        print(*sorted(group))


if __name__ == '__main__':
    main()
