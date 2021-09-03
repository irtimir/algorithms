"""
На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв,
которые можно набрать такой последовательностью нажатий.
"""

import sys

D_TO_S = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def combinations(seq, n=0, prefix=''):
    if n == len(seq):
        yield prefix
    else:
        for s in seq[n]:
            yield from combinations(seq, n + 1, prefix + s)


def main():
    seq = [D_TO_S[s] for s in sys.stdin.readline().rstrip()]
    print(*combinations(seq))


if __name__ == '__main__':
    main()
