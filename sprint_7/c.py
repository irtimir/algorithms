"""
C. Золотая лихорадка
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Гуляя по одному из островов Алгосского архипелага, Гоша набрёл на пещеру, в которой лежат кучи золотого песка.
К счастью, у Гоши есть с собой рюкзак грузоподъёмностью до M килограмм, поэтому он может унести с собой какое-то
ограниченное количество золота.

Всего золотых куч n штук, и все они разные. В куче под номером i содержится mi килограммов золотого песка, а стоимость
одного килограмма — ci алгосских франков.

Помогите Гоше наполнить рюкзак так, чтобы общая стоимость золотого песка в пересчёте на алгосские франки была
максимальной.

Формат ввода
В первой строке задано целое число M — грузоподъёмность рюкзака Гоши (0 ≤ M ≤ 108).

Во второй строке дано количество куч с золотым песком — целое число n (1 ≤ n ≤ 105).

В каждой из следующих n строк описаны кучи: i-ая куча задаётся двумя целыми числами ci и mi, записанными через пробел
(1 ≤ ci ≤ 107, 1 ≤ mi ≤ 108).

Формат вывода
Выведите единственное число —– максимальную сумму (в алгосских франках), которую Гоша сможет вынести из пещеры в своём
рюкзаке.
"""

import sys
from collections import namedtuple


HeapData = namedtuple('HeapData', ('price', 'weight'))


def main():
    m = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    heaps = []

    for _ in range(n):
        heaps.append(HeapData(*map(int, sys.stdin.readline().rstrip().split())))

    heaps.sort(key=lambda h: (-h.price, -h.weight))

    profit = 0
    current_m = 0

    for heap in heaps:
        available_m = m - current_m

        if available_m == 0:
            break
        elif available_m >= heap.weight:
            current_m += heap.weight
            profit += heap.price * heap.weight
        else:
            current_m += available_m
            profit += heap.price * available_m

    print(profit)


if __name__ == '__main__':
    main()
