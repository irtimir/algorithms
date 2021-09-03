"""
Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи есть копилка, в которую
каждый день он может добавлять деньги (если, конечно, у него есть такая финансовая возможность).
В процессе накопления Вася не вынимает деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить
первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.

Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке неубывания.
Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда. Это число не превосходит 106.

1 2 4 6 8 9 10 12 13
"""

import sys


def find_idx(incomes, amount, left, right):
    left_value = incomes[left]

    if left_value >= amount:
        return left + 1

    right_value = incomes[right - 1]

    if right_value < amount:
        return -1

    mid = (left + right) // 2

    mid_left_value = incomes[mid - 1]

    if mid_left_value >= amount:
        return find_idx(incomes, amount, left, mid)
    else:
        return find_idx(incomes, amount, mid, right)


def find_two_idxs(incomes, amount, amount_2, left, right):
    right_value = incomes[right - 1]

    if right_value < amount:
        return -1, -1

    if right_value < amount_2:
        return find_idx(incomes, amount, left, right), -1

    if incomes[left] >= amount_2:
        return left + 1, left + 1

    mid = (left + right) // 2
    mid_left_value = incomes[mid - 1]

    if mid_left_value >= amount:
        amount_left = left
        amount_right = mid
    else:
        amount_left = mid
        amount_right = right

    if mid_left_value >= amount_2:
        amount_2_left = left
        amount_2_right = mid
    else:
        amount_2_left = mid
        amount_2_right = right

    if (amount_left == amount_2_left) and (amount_right == amount_2_right):
        return find_two_idxs(incomes, amount, amount_2, amount_left, amount_right)
    else:
        return (
            find_idx(incomes, amount, amount_left, amount_right),
            find_idx(incomes, amount_2, amount_2_left, amount_2_right),
        )


def main():
    days_count = int(sys.stdin.readline().rstrip())
    incomes = list(map(int, sys.stdin.readline().rstrip().split()))
    amount = int(sys.stdin.readline().rstrip())

    print(*find_two_idxs(incomes, amount, amount * 2, 0, days_count))


if __name__ == '__main__':
    main()


def test_helper(incomes, amount):
    return find_two_idxs(incomes, amount, amount * 2, 0, len(incomes))


def test():
    assert test_helper([1, 2, 4, 4, 6, 8], 3) == (3, 5)
    assert test_helper([1, 2, 4, 4, 4, 4], 3) == (3, -1)
    assert test_helper([1, 2, 4, 4, 4, 4], 10) == (-1, -1)
    assert test_helper([1], 10) == (-1, -1)
    assert test_helper([20], 10) == (1, 1)
    assert test_helper([10], 10) == (1, -1)
    assert test_helper([1, 2, 3, 4, 5], 1) == (1, 2)
    assert test_helper([0, 0, 0, 0, 0, 1, 2], 1) == (6, 7)
    assert test_helper([1, 2, 3, 6, 8, 9], 3) == (3, 4)
    assert test_helper([1, 1, 1, 1, 1, 2], 1) == (1, 6)
