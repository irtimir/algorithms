"""
Метеорологическая служба вашего города решила исследовать погоду новым способом.
Под температурой воздуха в конкретный день будем понимать максимальную температуру в этот день.
Назовём хаотичностью погоды за n дней количество дней, в которые температура строго больше,
чем в день до (если такой существует) и в день после текущего (если такой существует).
Например, если за 5 дней максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

Заметим, что если если число показаний n=1, то единственный день будет хаотичным.

Формат ввода
В первой строке дано число n –— длина периода измерений в днях, 1 ≤ n≤ 105.
Во второй строке даны n целых чисел –— значения температуры в каждый из n дней.
Значения температуры не превосходят 273 по модулю.
"""

import sys


def main():
    length = int(sys.stdin.readline().rstrip())
    indications = list(map(int, sys.stdin.readline().rstrip().split()))

    if length == 1:
        print(1)
        return

    counter = 0

    if indications[0] > indications[1]:
        counter += 1

    if indications[length - 1] > indications[length - 2]:
        counter += 1

    for prev_idx in range(length - 2):
        curr_idx = prev_idx + 1
        next_idx = prev_idx + 2
        if indications[curr_idx] > indications[prev_idx] and indications[curr_idx] > indications[next_idx]:
            counter += 1

    print(counter)


if __name__ == '__main__':
    main()
