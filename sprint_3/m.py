"""
M. Золотая середина
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	0.058 секунд	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	0.084 секунды	64Mb
Oracle Java 8	0.18 секунд	64Mb
OpenJDK Java 11	0.18 секунд	64Mb
Node JS 8.16	0.084 секунды	64Mb
Задача повышенной сложности

На каждом острове в архипелаге Алгосы живёт какое-то количество людей или же остров необитаем (тогда на острове живёт
0 людей). Пусть на i-м острове численность населения составляет ai. Тимофей захотел найти медиану среди всех значений
численности населения.

Определение: Медиана (https://ru.wikipedia.org/wiki/Медиана_(статистика)) массива чисел a_i —– это такое число, что
половина чисел из массива не больше него, а другая половина не меньше. В общем случае медиану массива можно найти,
отсортировав числа и взяв среднее из них. Если количество чисел чётно, то возьмём в качестве медианы полусумму
соседних средних чисел, (a[n/2] + a[n/2 + 1])/2.

У Тимофея уже есть отдельно данные по северной части архипелага и по южной, причём значения численности населения в
каждой группе отсортированы по неубыванию.

Определите медианную численность населения по всем островам Алгосов.

Подсказка: Если n –— число островов в северной части архипелага, а m –— в южной, то ваше решение должно работать за .

Формат ввода
В первой строке записано натуральное число n, во второй —– натуральное число m. Они не превосходят 10 000.

Далее в строку через пробел записаны n целых неотрицательных чисел, каждое из которых не превосходит 10 000, –—
значения численности населения в северной части Алгосов.

В последней строке через пробел записаны m целых неотрицательных чисел, каждое из которых не превосходит 10 000 –—
значения численности населения в южной части Алгосов.

Значения в третьей и четвёртой строках упорядочены по неубыванию.

Формат вывода
Нужно вывести одной число — найденную медиану.
"""

import sys


def merge_iter(arr1, arr2):
    l = 0
    r = 0

    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            yield arr1[l]
            l += 1
        else:
            yield arr2[r]
            r += 1

    for i in range(l, len(arr1)):
        yield arr1[i]

    for i in range(r, len(arr2)):
        yield arr2[i]


def median(arr1, arr2):
    # target_idxs = []
    # target_idxs.append((len(arr1) + len(arr2)) // 2)
    #
    # if (len(arr1) + len(arr2)) % 2 == 0:
    #     target_idxs.append(target_idxs[0] - 1)
    #
    # values = []
    #
    # for n, val in enumerate(merge_iter(arr1, arr2)):
    #     if n in target_idxs:
    #         values.append(val)
    #
    #     if len(values) == len(target_idxs):
    #         return sum(values) / len(values)

    if (len(arr1) + len(arr2)) % 2 == 0:
        target_1_idx = (len(arr1) + len(arr2)) // 2
        target_2_idx = target_1_idx - 1
        target_1 = None
        target_2 = None
        for n, val in enumerate(merge_iter(arr1, arr2)):
            if n == target_1_idx:
                target_1 = val
            if n == target_2_idx:
                target_2 = val

            if target_1 is not None and target_2 is not None:
                return (target_1 + target_2) / 2
    else:
        target_idx = (len(arr1) + len(arr2)) // 2

        for n, val in enumerate(merge_iter(arr1, arr2)):
            if n == target_idx:
                return val


def main():
    n = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())

    north = list(map(int, sys.stdin.readline().rstrip().split()))
    south = list(map(int, sys.stdin.readline().rstrip().split()))

    print('{0:g}'.format(median(north, south)))


if __name__ == '__main__':
    main()
