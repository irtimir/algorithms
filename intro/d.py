"""
Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения этой задачи.
Помогите ей написать программу для поиска нужных фишек.
"""


def two_sum_simple(numbers, X):
    for i, n1 in enumerate(numbers):
        for n2 in numbers[i+1:]:
            if n1 + n2 == X:
                return f'{n1} {n2}'
    return


def main():
    # _ = input()
    # numbers = list(map(int, input().split(' ')))
    # X = int(input())
    numbers = list(map(int, '-3 1 1 2 6 6 8 10'.split(' ')))
    X = int(100)

    print(two_sum_simple(numbers, X))


if __name__ == '__main__':
    main()
