"""
E. Вставка строк
Все языки	GNU c++17 7.3
Ограничение времени	1 секунда	0.2 секунды
Ограничение памяти	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
У Риты была строка s, Гоша подарил ей на 8 марта ещё n других строк ti, 1≤ i≤ n. Теперь Рита думает, куда их лучше
поставить. Один из вариантов —– расположить подаренные строки внутри имеющейся строки s, поставив строку ti сразу после
символа строки s с номером ki (в частности, если ki=0, то строка вставляется в самое начало s).

Помогите Рите и определите, какая строка получится после вставки в s всех подаренных Гошей строк.

Формат ввода
В первой строке дана строка s. Строка состоит из строчных букв английского алфавита, не бывает пустой и её длина не
превышает 105 символов.

Во второй строке записано количество подаренных строк — натуральное число n, 1 ≤ n ≤ 105.

В каждой из следующих n строк через пробел записаны пары ti и ki. Строка ti состоит из маленьких латинских букв и не
бывает пустой. ki — целое число, лежащее в диапазоне от 0 до |s|. Все числа ki уникальны. Гарантируется, что суммарная
длина всех строк ti не превосходит 105.

Формат вывода
Выведите получившуюся в результате вставок строку.
"""

import sys


def main():
    s = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    to_insert = {}

    for _ in range(n):
        t, k = sys.stdin.readline().rstrip().split()
        k = int(k)

        to_insert[k] = t

    res = []

    for n, s_i in enumerate(s):
        if n == 0:
            res.append(to_insert.get(0, '') + s_i + to_insert.get(1, ''))
        else:
            res.append(s_i + to_insert.get(n + 1, ''))

    print(''.join(res))


if __name__ == '__main__':
    main()
