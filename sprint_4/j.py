"""
J. Сумма четвёрок
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	2 секунды	128Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	2 секунды	170Mb
Python 3.7.3	2 секунды	170Mb
Oracle Java 8	3.2 секунды	788Mb
OpenJDK Java 11	3.2 секунды	788Mb
Node JS 8.16	2 секунды	170Mb
У Гоши есть любимое число S. Помогите ему найти все уникальные четвёрки чисел в массиве, которые в сумме дают
заданное число S.

Формат ввода
В первой строке дано общее количество элементов массива n (0 ≤ n ≤ 1000).

Во второй строке дано целое число S  .

В третьей строке задан сам массив. Каждое число является целым и не превосходит по модулю 109.

Формат вывода
В первой строке выведите количество найденных четвёрок чисел.

В последующих строках выведите найденные четвёрки. Числа внутри одной четверки должны быть упорядочены по возрастанию.
Между собой четвёрки упорядочены лексикографически.
"""

import sys


def four_sum(nums, target):
    l = len(nums)
    d = {}
    res = set()
    nums.sort()
    for i in range(l - 1):
        for j in range(i + 1, l):
            key = nums[i] + nums[j]
            if key not in d:
                d[key] = [(i, j)]
            else:
                d[key].append((i, j))
    for i in range(2, l - 1):
        for j in range(i + 1, l):
            pre = target - nums[i] - nums[j]
            if pre in d:
                for v in d[pre]:
                    if v[1] < i:
                        res.add((nums[v[0]], nums[v[1]], nums[i], nums[j]))

    res = list(res)
    res.sort()

    return res


def main():
    length = int(sys.stdin.readline().rstrip())
    target = int(sys.stdin.readline().rstrip())
    raw_seq = sys.stdin.readline().rstrip()

    if length > 0:
        seq = list(map(int, raw_seq.split(' ')))
    else:
        seq = []

    seq.sort()

    res = four_sum(seq, target)
    print(len(res))
    for r in res:
        print(' '.join(map(str, r)))


if __name__ == '__main__':
    main()
