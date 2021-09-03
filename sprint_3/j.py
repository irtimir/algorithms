"""
Чтобы выбрать самый лучший алгоритм для решения задачи, Гоша продолжил изучать разные сортировки.
На очереди сортировка пузырьком — https://ru.wikipedia.org/wiki/Сортировка_пузырьком

Её алгоритм следующий (сортируем по неубыванию):

На каждой итерации проходим по массиву, поочередно сравнивая пары соседних элементов.
Если элемент на позиции i больше элемента на позиции i + 1, меняем их местами.
После первой итерации самый большой элемент всплывёт в конце массива.
Проходим по массиву, выполняя указанные действия до тех пор, пока на очередной итерации не окажется,
что обмены больше не нужны, то есть массив уже отсортирован.
После не более чем n – 1 итераций выполнение алгоритма заканчивается, так как на каждой итерации
хотя бы один элемент оказывается на правильной позиции.

Помогите Гоше написать код алгоритма.
Формат ввода
В первой строке на вход подаётся натуральное число n — длина массива, 2 ≤ n ≤ 1000.
Во второй строке через пробел записано n целых чисел.
Каждое из чисел по модулю не превосходит 1000.

Обратите внимание, что считывать нужно только 2 строки: значение n и входной массив.
"""

import sys


def bubble_sort(seq):
    for iter_ in range(len(seq) - 1):
        changed = False
        for idx in range(len(seq) - iter_ - 1):
            if seq[idx] > seq[idx + 1]:
                changed = True
                seq[idx], seq[idx + 1] = seq[idx + 1], seq[idx]

        if changed:
            yield ' '.join(map(str, seq))


def main():
    count = int(sys.stdin.readline().rstrip())
    seq = list(map(int, sys.stdin.readline().rstrip().split()))

    print(*(list(bubble_sort(seq)) or [' '.join(map(str, seq))]), sep='\n')


if __name__ == '__main__':
    main()

"""
5
4 3 9 2 1

5
8 9 10 11 12
"""