"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.
"""

import sys
# from itertools import zip_longest


def bubble_sort(seq, key):
    for iter_ in range(len(seq) - 1):
        for idx in range(len(seq) - iter_ - 1):
            if key(seq[idx], seq[idx + 1]):
                seq[idx], seq[idx + 1] = seq[idx + 1], seq[idx]


def key(a, b):
    return int(b + a) > int(a + b)
    # if len(a) == len(b):
    #     return a < b
    # for a1, b1 in zip_longest(a, b):
    #     if a1 is None or b1 is None:
    #         return int(b + a) > int(a + b)
    #
    #     if a1 == b1:
    #         continue
    #     return a1 < b1


def main():
    n = int(sys.stdin.readline().rstrip())
    digits = sys.stdin.readline().rstrip().split()
    bubble_sort(digits, key=key)
    print(''.join(digits))


if __name__ == '__main__':
    main()


"""
30
9 18 1 65 51 16 6 43 6 36 7 11 64 5 1 76 15 11 11 15 57 95 3 49 92 78 83 51 10 3
995928378776666564575515149433633181615151111111110
"""
