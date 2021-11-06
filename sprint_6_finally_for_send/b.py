"""
Run ID: 55989297

-- ПРИНЦИП РАБОТЫ --
Храним рёбра в списках смежности, если для одного из типов дороги менять направление ребра, то в итоге получим один
граф, для каждой вершины запускаем обход DFS, если граф имеет цикл, значит путь неоптимальный.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Как в DFS со списками смежности: O(V+E)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Список смежности - O(E * V), где E - количество вершин, V - количество рёбер
"""

import sys

WHITE = 0
GRAY = 1
BLACK = 2


class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def dfs_is_cyclic(start_vertex, adjacency, colors):
    stack = Stack()
    stack.push(start_vertex)

    while stack:
        v = stack.pop()
        if colors[v] == WHITE:
            colors[v] = GRAY
            stack.push(v)

            for w in adjacency[v]:
                if colors[w] == GRAY:
                    return True
                if colors[w] == WHITE:
                    stack.push(w)
        elif colors[v] == GRAY:
            colors[v] = BLACK

    return False


def is_cyclic(adjacency):
    colors = [WHITE] * len(adjacency)
    for i in range(len(adjacency)):
        if dfs_is_cyclic(i, adjacency, colors):
            return True
    return False


def main():
    n = int(sys.stdin.readline().rstrip())

    adjacency = {v: [] for v in range(0, n)}

    for i in range(n - 1):
        for j, klass in enumerate(sys.stdin.readline().rstrip()):
            if klass == 'B':
                adjacency[i].append(i + j + 1)
            elif klass == 'R':
                adjacency[i + j + 1].append(i)
            else:
                raise ValueError('Unknown road type.')

    if is_cyclic(adjacency):
        print('NO')
    else:
        print('YES')


if __name__ == '__main__':
    main()
