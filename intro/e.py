"""
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Фишки лежат на столе в порядке неубывания очков на них.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.

"""


def two_sum_extra_ds(numbers: list, X: int):
    previous = set()

    for n1 in numbers:
        n2 = X - n1
        if n2 in previous:
            return f'{n1} {n2}'
        else:
            previous.add(n1)

    return


def two_sum_with_sort(numbers: list, X: int):
    numbers.sort()

    left = 0
    right = len(numbers) - 1

    while left != right:
        n1, n2 = numbers[left], numbers[right]
        s = n1 + n2
        if s == X:
            return f'{n1} {n2}'

        if s < X:
            left += 1
        else:
            right -= 1

    return


def main():
    # _ = input()
    # numbers = list(map(int, input().split(' ')))
    # X = int(input())
    numbers = list(map(int, '-3 1 1 2 6 6 8 10'.split(' ')))
    X = int(100)

    print(two_sum_with_sort(numbers, X))
    print(two_sum_extra_ds(numbers, X))


if __name__ == '__main__':
    main()
