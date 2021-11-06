"""
A. Дорогая сеть
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.2 секунды	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	0.5 секунд	64Mb
Python 3.7.3	1.3 секунды	64Mb
Mono C# 5.2.0	0.7 секунд	64Mb
Oracle Java 8	0.7 секунд	64Mb
OpenJDK Java 11	0.7 секунд	64Mb
Node JS 8.16	0.5 секунд	64Mb
Тимофей решил соединить все компьютеры в своей компании в единую сеть. Для этого он придумал построить минимальное
остовное дерево, чтобы эффективнее использовать ресурсы.

Но от начальства пришла новость о том, что выделенный на сеть бюджет оказался очень большим и его срочно надо
израсходовать. Поэтому Тимофея теперь интересуют не минимальные, а максимальные остовные деревья.

Он поручил вам найти вес такого максимального остовного дерева в неориентированном графе, который задаёт схему офиса.

Формат ввода
В первой строке дано количество вершин n и ребер m графа (1 ≤ n ≤ 1000, 0 ≤ m ≤ 100000).

В каждой из следующих m строк заданы рёбра в виде троек чисел u, v, w. u и v — вершины, которые соединяет это ребро.
w — его вес ( 1 ≤ u, v ≤ n, 0 ≤ w ≤ 10000). В графе могут быть петли и кратные ребра. Граф может оказаться несвязным.

Формат вывода
Если максимальное остовное дерево существует, то выведите его вес. Иначе (если в графе несколько компонент связности)
выведите фразу «Oops! I did it again».

Run ID: 55961560
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
