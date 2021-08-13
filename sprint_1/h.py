"""
Тимофей спросил у Гоши, умеет ли тот работать с числами в двоичной системе счисления.
Он ответил, что проходил это на одной из первых лекций по информатике.
Тимофей предложил Гоше решить задачку. Два числа записаны в двоичной системе счисления.
Нужно вывести их сумму, также в двоичной системе.
Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.
"""
import itertools
import sys


sum_operations = {
    ('0', '0'): ('0', '0'),
    ('0', '1'): ('0', '1'),
    ('1', '0'): ('0', '1'),
    ('1', '1'): ('1', '0'),
}


def main():
    a = sys.stdin.readline().rstrip()[::-1]
    b = sys.stdin.readline().rstrip()[::-1]

    result = []
    extra_stack = 0

    for a, b in itertools.zip_longest(a, b, fillvalue='0'):
        s = sum_operations[(a, b)]
        extra = 1 if s[0] == '1' else 0
        res = s[1]

        if extra_stack > 0:
            s1 = sum_operations[(s[1], '1')]
            extra_stack -= 1
            if s1[0] == '1':
                extra_stack += 1
            res = s1[1]

        extra_stack += extra
        result.append(res)

    result.extend(['1' for _ in range(extra_stack)])
    result.reverse()
    print(''.join(result))


if __name__ == '__main__':
    main()
