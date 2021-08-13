"""
Помогите Васе понять, будет ли фраза палиндромом.
Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово.
Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.
"""

import sys


def main():
    symbols = sys.stdin.readline().rstrip()

    length = len(symbols)

    left_idx = 0
    right_idx = length - 1

    is_palindrom = True

    while left_idx < right_idx:
        left_symbol = symbols[left_idx].lower()
        right_symbol = symbols[right_idx].lower()

        if not left_symbol.isalnum():
            left_idx += 1
            continue

        if not right_symbol.isalnum():
            right_idx -= 1
            continue

        if left_symbol != right_symbol:
            is_palindrom = False
            break

        left_idx += 1
        right_idx -= 1

    print(is_palindrom)


if __name__ == '__main__':
    main()
