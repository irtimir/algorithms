"""
Рита решила оставить у себя одежду только трёх цветов: розового, жёлтого и малинового.
После того как вещи других расцветок были убраны, Рита захотела отсортировать свой новый гардероб по цветам.
Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового.
Помогите Рите справиться с этой задачей.

Примечание: попробуйте решить задачу за один проход по массиву!

Формат ввода
В первой строке задано количество предметов в гардеробе: n –— оно не превосходит 1000000.
Во второй строке даётся массив, в котором указан цвет для каждого предмета.
Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.
"""

import sys


def count_sort(seq):
    res = [0] * 3

    for elem in seq:
        res[elem] += 1

    return ([0] * res[0]) + ([1] * res[1]) + ([2] * res[2])


def main():
    sys.stdin.readline().rstrip()
    seq = list(map(int, sys.stdin.readline().rstrip().split()))
    print(*count_sort(seq))


if __name__ == '__main__':
    main()