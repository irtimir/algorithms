"""
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.

Но не всё так просто. Печенья могут быть разного размера. А у каждого ребёнка есть фактор жадности —–
минимальный размер печенья, которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными
в лучшем случае, когда они действуют оптимально.

Каждый ребёнок может взять не больше одного печенья.

Формат ввода
В первой строке записано n —– количество детей.

Во второй —– n чисел, разделённых пробелом, каждое из которых –— фактор жадности ребёнка.
Это натуральные числа, не превосходящие 1000.

В следующей строке записано число m –— количество печенек.

Далее —– m натуральных чисел, разделённых пробелом —– размеры печенек.
Размеры печенек не превосходят 1000.

Оба числа n и m не превосходят 10000.
"""

import sys


def funny_count(greed_factor, cookies):
    greed_factor.sort()
    cookies.sort()

    count = 0

    for cookie in cookies:
        if count == len(greed_factor):
            break
        if greed_factor[count] <= cookie:
            count += 1

    return count


def main():
    n = int(sys.stdin.readline().rstrip())
    greed_factor = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    cookies = list(map(int, sys.stdin.readline().rstrip().split()))
    print(funny_count(greed_factor, cookies))


if __name__ == '__main__':
    main()
