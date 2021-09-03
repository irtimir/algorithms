"""
Run ID: 52518416

-- ПРИНЦИП РАБОТЫ --
Алгоритм выбирает опорный элемент из середины массива и элементы меньше опорного перемещаются влево, а элементы больше
вправо, далее массив делится на 2 части до опорного элемента и после и для каждоый части рекурсивно вызывается
сортировка.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Опорный элемент выбирается из массива, таким образом гарантируется остановка указателей. Указатели останавливаются
тогда, когда один из указателей перейдёт за другой.
Базовый случай рекурсии когда сортируемая часть последовательности состоит из одного элемента - это значит что
последовательность не надо сортировать.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Алгоритм исключает сложность O(N^2) на отсортированном списке, потомоу что опорный элемент выбирается из середины
массива.  Таким образом на каждом шаге будет сделано O(N) операций. Глубина рекурсии составляет O(logN), таким образом
общая сложность составляет O(NlogN)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Оперативная память используется только для хранения элементов исходного массива, поэтому алгоритм будет
потреблять O(N) памяти.
"""

import sys


def quicksort_inplace(seq, left, right):
    l_pointer = left
    r_pointer = right - 1

    if right - left == 1:
        return

    pivot = seq[left + (right - left) // 2]

    while True:
        while seq[l_pointer] < pivot:
            l_pointer += 1

        while seq[r_pointer] > pivot:
            r_pointer -= 1

        if l_pointer > r_pointer - 1:
            break

        seq[l_pointer], seq[r_pointer] = seq[r_pointer], seq[l_pointer]
        l_pointer += 1
        r_pointer -= 1

    quicksort_inplace(seq, left, l_pointer)
    quicksort_inplace(seq, l_pointer, right)


def main():
    n = int(sys.stdin.readline().rstrip())
    data = []

    for _ in range(n):
        login, tasks_done, fine = sys.stdin.readline().rstrip().split()
        data.append((-int(tasks_done), int(fine), login))

    quicksort_inplace(data, 0, len(data))
    print(*map(lambda i: i[2], data), sep='\n')


if __name__ == '__main__':
    main()
