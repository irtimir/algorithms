"""
Run ID: 52518416
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


def test():
    a = [2, 1]
    quicksort_inplace(a, 0, len(a))
    assert a == [1, 2]

    a = [4, 8, 9, 20, 1, 5, 3, 10]
    quicksort_inplace(a, 0, len(a))
    assert a == [1, 3, 4, 5, 8, 9, 10, 20]

    a = [1, 1, 1, 1, 1]
    quicksort_inplace(a, 0, len(a))
    assert a == [1, 1, 1, 1, 1]

    a = [1, 1, 2, 1, 1, 1]
    quicksort_inplace(a, 0, len(a))
    assert a == [1, 1, 1, 1, 1, 2]

    a = [1, 3, 1, 2, 1, 6, 1, 2, 1]
    quicksort_inplace(a, 0, len(a))
    assert a == [1, 1, 1, 1, 1, 2, 2, 3, 6]


if __name__ == '__main__':
    test()
