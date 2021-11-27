"""
K. Сравнить две строки
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Алла придумала новый способ сравнивать две строки: чтобы сравнить строки a и b, в них надо оставить только те буквы,
которые в английском алфавите стоят на четных позициях. Затем полученные строки сравниваются по обычным правилам.
Помогите Алле реализовать новое сравнение строк.

Формат ввода
На вход подаются строки a и b по одной в строке. Обе строки состоят из маленьких латинских букв, не бывают пустыми и не
превосходят 105 символов в длину.

Формат вывода
Выведите -1, если a < b, 0, если a = b, и 1, если a > b.
"""

import sys
import string


def main():
    a = sys.stdin.readline().rstrip()
    b = sys.stdin.readline().rstrip()

    valid_symbols = []

    for n, s in enumerate(string.ascii_lowercase):
        if (n + 1) % 2 == 0:
            valid_symbols.append(s)

    a_f = ''.join(filter(lambda e: e in valid_symbols, a))
    b_f = ''.join(filter(lambda e: e in valid_symbols, b))

    if a_f == b_f:
        print(0)
    elif a_f > b_f:
        print(1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
