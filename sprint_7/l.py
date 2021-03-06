"""
L. Золото лепреконов
Все языки	Python 3.7.3
Ограничение времени	1 секунда	2.5 секунд
Ограничение памяти	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Лепреконы в данной задаче появились по соображениям общей морали, так как грабить банки — нехорошо.

Вам удалось заключить неплохую сделку с лепреконами, поэтому они пустили вас в своё хранилище золотых слитков. Все
слитки имеют единую пробу, то есть стоимость 1 грамма золота в двух разных слитках одинакова. В хранилище есть n
слитков, вес i-го слитка равен wi кг. У вас есть рюкзак, вместимость которого M килограмм.

Выясните максимальную суммарную массу золотых слитков, которую вы сможете унести.

Формат ввода
В первой строке дано число слитков —– натуральное число n (1 ≤ n ≤ 1000) и вместимость рюкзака –— целое число M
(0 ≤ M ≤ 104). Во второй строке записано n натуральных чисел wi (1 ≤ wi ≤ 104) -— массы слитков.

Формат вывода
Выведите единственное число — максимальную массу, которую можно забрать с собой.
"""

import sys


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    w = list(map(int, sys.stdin.readline().rstrip().split()))
    w.sort(reverse=True)

    dp = [False for _ in range(m)]

    for i in range(len(w)):
        if w[i] <= m:
            dp[w[i] - 1] = True

        for j in range(len(dp) - 1, -1, -1):
            if j == 99 and dp[j - w[i]]:
                print(1)

            if j - w[i] >= 0 and dp[j - w[i]]:
                dp[j] = True

    print(dp)

    for n in range(len(dp) - 1, -1, -1):
        if dp[n]:
            print(n + 1)
            break
    else:
        print(0)


if __name__ == '__main__':
    main()
