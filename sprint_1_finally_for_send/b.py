"""
Run ID: 52332427
"""
import sys
from collections import Counter


def get_score(k, matrix):
    max_elements = k * 2
    score = 0
    c = Counter()

    for line in matrix:
        c.update(line)

    c.pop('.', None)

    for v in c.values():
        if v <= max_elements:
            score += 1

    return score


def main():
    k = int(sys.stdin.readline().rstrip())
    matrix = []

    for _ in range(4):
        matrix.append(list(sys.stdin.readline().rstrip()))

    print(get_score(k, matrix))


if __name__ == '__main__':
    main()
