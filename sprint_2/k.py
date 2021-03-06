"""
У Тимофея было n (0≤n≤32) стажёров. Каждый стажёр хотел быть лучше своих предшественников, поэтому i-й стажёр делал
столько коммитов, сколько делали два предыдущих стажёра в сумме. Два первых стажёра были менее
инициативными —– они сделали по одному коммиту.
Пусть Fi —– число коммитов, сделанных i-м стажёром (стажёры нумеруются с нуля). Тогда выполняется следующее:
F0=F1=1. Для всех i≥2  выполнено Fi=Fi−1+Fi−2.
Определите, сколько кода напишет следующий стажёр –— найдите Fn.
Решение должно быть реализована рекурсивно.
"""

import sys


def fib(n):
    if n in (0, 1):
        return 1

    return fib(n - 1) + fib(n - 2)


def main():
    n = int(sys.stdin.readline().rstrip())
    print(fib(n))


if __name__ == '__main__':
    main()
