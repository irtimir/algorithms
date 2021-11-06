"""
Run ID: 55961560

-- ПРИНЦИП РАБОТЫ --
Собираем неориентированный граф на списках смежности, для оптимальности, используем словарь с ключами - вершинами из
которых выходят рёбра. Далее, составляет остовное дерево, храня самое "тяжёлое" ребро в куче, используя встроенную
реализацию heapq.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(E*logV), где E - количество рёбер в графе, а V - количество вершин

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Хранение кучи - O(n)
Список смежности - O(E * V), где E - количество вершин, V - количество рёбер
"""

import heapq
import sys
from collections import namedtuple, defaultdict

Graph = namedtuple('Graph', ['vertices', 'edges'])
EdgeData = namedtuple('EdgeData', ['f', 't', 'weight'])
EdgePriority = namedtuple('EdgePriority', ['value', 'edge'])


def extract_maximum(edges):
    return heapq.heappop(edges).edge


def add_vertex(v, graph, added, not_added, edges):
    added.add(v)
    not_added.remove(v)

    for edge in graph.edges.get(v, []):
        if edge.t in not_added:
            heapq.heappush(edges, EdgePriority(-edge.weight, edge))


def find_max_st(graph):
    max_spanning_tree = []
    added = set()
    not_added = set(graph.vertices)
    edges = []
    v = graph.vertices[0]
    add_vertex(v, graph, added, not_added, edges)

    while not_added and edges:
        e = extract_maximum(edges)
        if e.t in not_added:
            max_spanning_tree.append(e)
            add_vertex(e.t, graph, added, not_added, edges)

    if not_added:
        raise ValueError('Oops! I did it again')

    return max_spanning_tree


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    graph = Graph(vertices=list(range(1, n + 1)), edges=defaultdict(list))

    for _ in range(m):
        f, t, w = map(int, sys.stdin.readline().rstrip().split())

        for edge_data in (EdgeData(f=f, t=t, weight=w), EdgeData(f=t, t=f, weight=w)):
            graph.edges[edge_data.f].append(edge_data)

    try:
        print(sum(map(lambda e: e.weight, find_max_st(graph))))
    except ValueError as exc:
        print(str(exc))


if __name__ == '__main__':
    main()
