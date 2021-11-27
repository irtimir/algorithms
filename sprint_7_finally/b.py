"""
B. Одинаковые суммы
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.05 секунд	8Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	0.4 секунды	100Mb
Python 3.7.3	1.5 секунд	8Mb
Mono C# 5.2.0	0.2 секунды	64Mb
Oracle Java 8	0.15 секунд	64Mb
OpenJDK Java 11	0.2 секунды	64Mb
Node JS 8.16	0.4 секунды	100Mb
На Алгосах устроили турнир по настольному теннису. Гоша выиграл n партий, получив при этом некоторое количество очков
за каждую из них.

Гоше стало интересно, можно ли разбить все заработанные им во время турнира очки на две части так, чтобы сумма в них
была одинаковой.

Формат ввода
В первой строке записано целое число n (0 ≤ n ≤ 300) –— количество выигранных партий.

Во второй строке через пробел записано n целых неотрицательных чисел, каждое из которых не превосходит 300 –—
заработанные в партиях очки.

Формат вывода
Нужно вывести True, если произвести такое разбиение возможно, иначе —– False
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
