"""
H. Глобальная замена
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Напишите программу, которая будет заменять в тексте все вхождения строки s на строку t. Гарантируется, что никакие два
вхождения шаблона s не пересекаются друг с другом.

Формат ввода
В первой строке дан текст —– это строка из строчных букв английского алфавита, длина которой не превышает 106.

Во второй строке записан шаблон s, вхождения которого будут заменены.

В третьей строке дана строка t, которая будет заменять вхождения.

Обе строки s и t состоят из строчных букв английского алфавита, длина каждой строки не превосходит 105. Размер итоговой
строки не превосходит 2⋅ 106.

Формат вывода
В единственной строке выведите результат всех замен — текст, в котором все вхождения s заменены на t.
"""


def find(p, text):
    result = []
    s = p + '#' + text
    pi = [0 for _ in range(len(p))]

    pi_prev = 0

    for i in range(1, len(s)):
        k = pi_prev
        while (k > 0) and (s[k] != s[i]):
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1

        if i < len(p):
            pi[i] = k

        pi_prev = k

        if k == len(p):
            result.append((i - 2 * len(p)))

    return result


import sys


def replace(text, old, new):
    s = old + '#' + text
    pi = [0 for _ in range(len(old))]
    pi_prev = 0
    result = []

    for i in range(1, len(s)):
        k = pi_prev
        while (k > 0) and (s[k] != s[i]):
            k = pi[k - 1]
        if s[k] == s[i]:
            k += 1
        if i < len(old):
            pi[i] = k

        if i > len(old):
            result.append(s[i])

        pi_prev = k

        if k == len(old):
            for _ in range(len(old)):
                result.pop()

            for new_s in new:
                result.append(new_s)

    return ''.join(result)


def main():
    a = sys.stdin.readline().rstrip()
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()

    print(replace(a, s, t))


if __name__ == '__main__':
    main()
