"""
H. Время выходить
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	1.5 секунд	128Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	4 секунды	128Mb
Python 3.7.3	2 секунды	128Mb
Node JS 8.16	4 секунды	128Mb
Вам дан ориентированный граф. Известно, что все его вершины достижимы из вершины s=1. Найдите время входа и выхода при
обходе в глубину, производя первый запуск из вершины s. Считайте, что время входа в стартовую вершину равно 0.
Соседей каждой вершины обходите в порядке увеличения номеров.

Формат ввода
В первой строке дано число вершин n (1 ≤ n ≤ 2⋅ 105) и рёбер (0 ≤ m ≤ 2 ⋅ 105). В каждой из следующих m строк записаны
рёбра графа в виде пар (from, to), 1 ≤ from ≤ n — начало ребра, 1 ≤ to ≤ n — его конец. Гарантируется, что в графе нет
петель и кратных рёбер.

Формат вывода
Выведите n строк, в каждой из которых записана пара чисел tini, touti — время входа и выхода для вершины i.
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
    time = -1
    entry = [0] * len(adjacency)
    leave = [0] * len(adjacency)

    while stack.size():
        v = stack.pop()
        if colors[v - 1] == WHITE:
            time += 1
            entry[v - 1] = time
            colors[v - 1] = GRAY
            stack.push(v)

            for w in sorted(adjacency[v], reverse=True):
                if colors[w - 1] == WHITE:
                    stack.push(w)

        elif colors[v - 1] == GRAY:
            time += 1
            leave[v - 1] = time
            colors[v - 1] = BLACK

    return zip(entry, leave)


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adjacency = {v: [] for v in range(1, n + 1)}

    for _ in range(m):
        f, t = map(int, sys.stdin.readline().rstrip().split())
        adjacency[f].append(t)

    print(*map(lambda seq: ' '.join(map(str, seq)), dfs(1, adjacency)), sep='\n')


if __name__ == '__main__':
    main()
