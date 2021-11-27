"""
G. Поиск со сдвигом
Все языки	Python 3.7.3	GNU c++17 7.3
Ограничение времени	1.5 секунд	3 секунды	0.15 секунд
Ограничение памяти	64Mb	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гоша измерял температуру воздуха n дней подряд. В результате у него получился некоторый временной ряд. Теперь он хочет
посмотреть, как часто встречается некоторый шаблон в получившейся последовательности. Однако температура — вещь
относительная, поэтому Гоша решил, что при поиске шаблона длины m (a1, a2, ..., am) стоит также рассматривать сдвинутые
на константу вхождения. Это значит, что если для некоторого числа c в исходной последовательности нашёлся участок вида
(a1 + c, a2 + c, ... , am + c), то он тоже считается вхождением шаблона (a1, a2, ..., am).

По заданной последовательности измерений X и шаблону A=(a1, a2, ..., am) определите все вхождения A в X, допускающие
сдвиг на константу.

Подсказка: если вы пишете на питоне и сталкиваетесь с TL, то попробуйте заменить какие-то из циклов операциями со
срезами.

Формат ввода
В первой строке дано количество сделанных измерений n — натуральное число, не превышающее 104. Во второй строке через
пробел записаны n целых чисел xi, 0 ≤ xi ≤ 103 –— результаты измерений. В третьей строке дано натуральное число m –—
длина искомого шаблона, 1≤ m ≤ n. В четвёртой строке даны m целых чисел ai — элементы шаблона, 0 ≤ ai ≤ 103.

Формат вывода
Выведите через пробел в порядке возрастания все позиции, на которых начинаются вхождения шаблона A в последовательность
X. Нумерация позиций начинается с единицы.
"""

import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))

    a_diff = []

    for n in range(len(a) - 1):
        a_diff.append(a[n + 1] - a[n])

    res = []

    for n in range(len(x) - len(a) + 1):
        match = True
        for offset in range(len(a) - 1):
            if x[n + offset + 1] - x[n + offset] != a_diff[offset]:
                match = False
                break

        if match:
            res.append(n)

    print(' '.join(map(str, map(lambda e: e + 1, res))))


if __name__ == '__main__':
    main()