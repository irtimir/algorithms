"""
B. Сломай меня
Гоша написал программу, которая сравнивает строки исключительно по их хешам. Если хеш равен, то и строки равны.
Тимофей увидел это безобразие и поручил вам сломать программу Гоши, чтобы остальным неповадно было.

В этой задаче вам надо будет лишь найти две различные строки, которые для заданной хеш-функции будут давать
одинаковое значение.

Гоша использует следующую хеш-функцию:


для a = 1000 и m = 123 987 123.
В данной задаче необходимо использовать в качестве значений отдельных символов их коды в таблице ASCII.

Формат ввода
В задаче единственный тест без ввода

Формат вывода
Отправьте две строки, по одной в строке. Строки могут состоять только из маленьких латинских букв и не должны превышать
в длину 1000 знаков каждая. Код отправлять не требуется. Строки из примера использовать нельзя.

Пример вывода:

ezhgeljkablzwnvuwqvp

gbpdcvkumyfxillgnqrv
"""
import string
import random


def polynom_hash(s, q, R):
    res = 0

    for sym in s:
        res = (res * q + ord(sym))

    return res % R


def main():
    q = 1000
    R = 123_987_123
    print(polynom_hash('ezhgeljkablzwnvuwqvp', q, R) == polynom_hash('gbpdcvkumyfxillgnqrv', q, R))

    s1 = list('ezhgeljkablzwnvuwqvp')
    s2 = list('gbpdcvkumyfxillgnqrv')

    while True:
        random.shuffle(s1)
        random.shuffle(s2)

        if polynom_hash(''.join(s1), q, R) == polynom_hash(''.join(s2), q, R):
            print(''.join(s1))
            print(''.join(s2))
            break


if __name__ == '__main__':
    main()
