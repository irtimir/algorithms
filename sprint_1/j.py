"""
Тимофей готовит доклад ко дню открытых дверей кафедры Теории чисел.
Он собирается рассказать про Основную теорему арифметики.
В соответствии с этой теоремой, любое число раскладывается на произведение
простых множителей единственным образом –— с точностью до их перестановки.

Например, число 8 можно представить как 2 × 2 × 2.

Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.

Разложение числа на простые множители называется факторизацией числа.

Факторизацию в уме делать сложно, поэтому помогите Тимофею написать для этого программу.

Формат ввода
В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.
"""
import sys


def get_min_divider(digit):
    sqrt_int = int(digit ** (1 / 2))

    for d in range(2, sqrt_int + 1):
        if digit % d == 0:
            return d


def brute_force(digit):
    res = []

    min_divider = get_min_divider(digit)

    if min_divider is None:
        res.append(digit)
    else:
        res.append(min_divider)
        res.extend(brute_force(digit // min_divider))

    return res


def main():
    digit = int(sys.stdin.readline().rstrip())

    res = brute_force(digit)
    res.sort()

    print(' '.join(map(str, res)))


if __name__ == '__main__':
    main()
