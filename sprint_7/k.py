"""
K. Гороскопы
Все языки	Python 3.7.3
Ограничение времени	0.3 секунды	2 секунды
Ограничение памяти	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В мире последовательностей нет гороскопов. Поэтому когда две последовательности хотят понять, могут ли они счастливо
жить вместе, они оценивают свою совместимость как длину их наибольшей общей подпоследовательности.

Подпоследовательность получается из последовательности удалением некоторого (возможно, нулевого) числа элементов. То
есть элементы сохраняют свой относительный порядок, но не обязаны изначально идти подряд.

Найдите наибольшую общую подпоследовательность двух одиноких последовательностей и выведите её!

Формат ввода
В первой строке дано число n — количество элементов в первой последовательности (1 ≤ n ≤ 1000). Во второй строке даны n
чисел ai (0 ≤ |ai| ≤ 109) — элементы первой последовательности. Аналогично в третьей строке дано m (1 ≤ m ≤ 1000) —
число элементов второй последовательности. В четвертой строке даны элементы второй последовательности через пробел bi
(0 ≤ |bi| ≤ 109).

Формат вывода
Сначала выведите длину найденной наибольшей общей подпоследовательности, во второй строке выведите индексы элементов
первой последовательности, которые в ней участвуют, в третьей строке — индексы элементов второй последовательности.
Нумерация индексов с единицы, индексы должны идти в корректном порядке.

Если возможных НОП несколько, то выведите любую.
"""

import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    a = sys.stdin.readline().rstrip().split()
    m = int(sys.stdin.readline().rstrip())
    b = sys.stdin.readline().rstrip().split()

    dp = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n][m])

    if not dp[n][m]:
        return

    result_a = []
    result_b = []
    i = n
    j = m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            result_a.append(i)
            result_b.append(j)
            i -= 1
            j -= 1
        elif dp[i - 1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1

    result_a.reverse()
    result_b.reverse()

    print(*result_a)
    print(*result_b)


if __name__ == '__main__':
    main()
