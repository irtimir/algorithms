"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

Например, в матрице A:
    0 1 2
0 | 1 2 3
1 | 0 2 6
2 | 7 4 1
3 | 2 7 0

соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m.
Числа m и n не превосходят 1000. В следующих n строках задана матрица.
Элементы матрицы — целые числа, по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента (индексация начинается с нуля), соседей которого нужно найти.
"""

import bisect
import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, sys.stdin.readline().rstrip().split())))

    y = int(sys.stdin.readline().rstrip())
    x = int(sys.stdin.readline().rstrip())

    min_idx_x = 0
    min_idx_y = 0

    max_idx_x = m - 1
    max_idx_y = n - 1

    neighbors = []

    if y != min_idx_y:
        bisect.insort(neighbors, matrix[y - 1][x])

    if y != max_idx_y:
        bisect.insort(neighbors, matrix[y + 1][x])

    if x != min_idx_x:
        bisect.insort(neighbors, matrix[y][x - 1])

    if x != max_idx_x:
        bisect.insort(neighbors, matrix[y][x + 1])

    print(' '.join(map(str, neighbors)))


if __name__ == '__main__':
    main()
