"""
Run id: 59179809

-- ПРИНЦИП РАБОТЫ --
Нулевой ряд и первый столбец матрицы - это просто восходящая последовательность, поэтому итерацию всегда начинаем с 1.
Соседние клетки матрицы отвечают за вставку удаление или замену символа (если символы неравны), выбираем
изменение с наименьшей стоимостью и зополняем ячейку, искомое значение будет в правом нижнем углу.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(A * B) , где A, B - это длина каждоый из строк

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Храним только части матрицы для текущей и предыдущей строк, получается O(N)
"""

import sys


def lev_dist(a, b):
    l_a, l_b = len(a), len(b)
    curr = range(l_a + 1)
    for i in range(1, l_b + 1):
        prev, curr = curr, [i] + [0] * l_a
        for j in range(1, l_a + 1):
            insert, remove, replace = prev[j] + 1, curr[j - 1] + 1, prev[j - 1]
            if a[j - 1] != b[i - 1]:
                replace += 1
            curr[j] = min(insert, remove, replace)
    return curr[l_a]


def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    print(lev_dist(a, b))


if __name__ == '__main__':
    main()
