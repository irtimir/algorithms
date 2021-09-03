"""
На IT-конференции присутствовали студенты из разных вузов со всей страны.
Для каждого студента известен ID университета, в котором он учится.

Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше всего учащихся.

Формат ввода
В первой строке дано количество студентов в списке —– n (1 ≤ n ≤ 15 000).

Во второй строке через пробел записаны n целых чисел —– ID вуза каждого студента.
Каждое из чисел находится в диапазоне от 0 до 10 000.

В третьей строке записано одно число k.
"""

import sys


def get_rating(seq):
    counter = {}
    for elem in seq:
        if elem in counter:
            counter[elem] = [counter[elem][0] + 1, -elem]
        else:
            counter[elem] = [1, -elem]

    results = list(counter.values())
    results.sort(reverse=True)

    return list(map(lambda i: abs(i[1]), results))


def main():
    count = int(sys.stdin.readline().rstrip())
    students = list(map(int, sys.stdin.readline().rstrip().split()))
    rate_count = int(sys.stdin.readline().rstrip())

    print(' '.join(map(str, get_rating(students)[:rate_count])))


if __name__ == '__main__':
    main()
