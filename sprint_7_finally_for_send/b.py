"""
Run id: 59237277

-- ПРИНЦИП РАБОТЫ --
В процессе поиска дополнительной информации наткнулся на такое описание алгоритма:
https://stackoverflow.com/questions/5898104/how-to-optimally-divide-an-array-into-two-subarrays-so-that-sum-of-elements-in-b/5898540#5898540

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(N * TotalSum), где N - количество элементов в массиве, а TotalSum - их общая сумма

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(TotalSum / 2) = O(TotalSum) - TotalSum - общая сумма всех элементов массива
"""

import sys


def terms_generator(numbers):
    sum_numbers = sum(numbers)
    dp = [-1] * (sum_numbers // 2 + 1)
    dp[0] = 0
    for number in numbers:
        for i in range(sum_numbers // 2, number - 1, -1):
            if dp[i] == -1 and dp[i - number] != -1:
                dp[i] = number
    if dp[sum_numbers // 2] == -1:
        raise ValueError
    curr = sum_numbers // 2
    while curr:
        yield dp[curr]
        curr -= dp[curr]


def get_equal_sums(numbers):
    terms_l = list(terms_generator(numbers))
    terms_r = list(numbers)
    for item in terms_l:
        terms_r.remove(item)
    if sum(terms_r) != sum(terms_l):
        raise ValueError
    return terms_r, terms_l


def main():
    sys.stdin.readline().rstrip()
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))

    try:
        get_equal_sums(numbers)
    except ValueError:
        print(False)
    else:
        print(True)


if __name__ == '__main__':
    main()
