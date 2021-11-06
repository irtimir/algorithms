"""
B. Железные дороги
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	2 секунды	256Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Golang 1.14.4 + network	4 секунды	256Mb
Node.js 14.15.5	5 секунд	256Mb
Python 3.7.3	12 секунд	700Mb
gc go	4 секунды	256Mb
Mono C# 5.2.0	3 секунды	512Mb
Oracle Java 8	3 секунды	512Mb
OpenJDK Java 11	3 секунды	512Mb
Golang 1.16	4 секунды	256Mb
Node JS 8.16	5 секунд	256Mb
В стране X есть n городов, которым присвоены номера от 1 до n. Столица страны имеет номер n. Между городами проложены
железные дороги.

Однако дороги могут быть двух типов по ширине полотна. Любой поезд может ездить только по одному типу полотна. Условно
один тип дорог помечают как R, а другой как B. То есть если маршрут от одного города до другого имеет как дороги типа
R, так и дороги типа B, то ни один поезд не сможет по этому маршруту проехать. От одного города до другого можно
проехать только по маршруту, состоящему исключительно из дорог типа R или только из дорог типа B.

Но это ещё не всё. По дорогам страны X можно двигаться только от города с меньшим номером к городу с большим номером.
Это объясняет большой приток жителей в столицу, у которой номер n.

Карта железных дорог называется оптимальной, если не существует пары городов A и B такой, что от A до B можно добраться
как по дорогам типа R, так и по дорогам типа B. Иными словами, для любой пары городов верно, что от города с меньшим
номером до города с бОльшим номером можно добраться по дорогам только какого-то одного типа или же что маршрут
построить вообще нельзя. Выясните, является ли данная вам карта оптимальной.

Формат ввода
В первой строке дано число n (1 ≤ n ≤ 5000) — количество городов в стране. Далее задана карта железных дорог в
следующей формате.

Карта задана n-1 строкой. В i-й строке описаны дороги из города i в города i+1, i+2, ..., n. В строке записано n - i
символов, каждый из которых либо R, либо B. Если j-й символ строки i равен «B», то из города i в город i + j идет
дорога типа «B». Аналогично для типа «R».

Формат вывода
Выведите «YES», если карта оптимальна, и «NO» в противном случае.
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
