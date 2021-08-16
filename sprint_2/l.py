"""
У Тимофея было очень много стажёров, целых N (0 ≤ N ≤ 106) человек. Каждый стажёр хотел быть лучше своих
предшественников, поэтому i-й стажёр делал столько коммитов, сколько делали два предыдущих стажёра в сумме.
Два первых стажёра были менее инициативными — они сделали по одному коммиту.

Пусть Fi —– число коммитов, сделанных i-м стажёром (стажёры нумеруются с нуля).
Первые два стажёра сделали по одному коммиту: F0=F1=1. Для всех i≥ 2 выполнено Fi=Fi−1+Fi−2.

Определите, сколько кода напишет следующий стажёр –— найдите последние k цифр числа Fn.


Как найти k последних цифр

Чтобы вычислить k последних цифр некоторого числа x, достаточно взять остаток от его деления на число 10k.
Эта операция обозначается как x mod 10k. Узнайте, как записывается операция взятия остатка
по модулю в вашем языке программирования.

Также обратите внимание на возможное переполнение целочисленных типов, если в вашем языке такое случается.

Формат ввода
В первой строке записаны через пробел два целых числа n (0 ≤ n ≤ 106) и k (1 ≤ k ≤ 8).
"""

import sys


def fib_last_numbers(n, k):
    if n in (0, 1):
        return 1

    a = 1
    b = 1
    c = None

    for _ in range(n - 1):
        c = (a + b) % 10**k
        a = b
        b = c

    return c


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())

    print(fib_last_numbers(n, k))


if __name__ == '__main__':
    main()