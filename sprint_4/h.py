"""
H. Странное сравнение
Все языки	Python 3.7.3
Ограничение времени	0.5 секунд	1 секунда
Ограничение памяти	64Mb	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Жители Алгосского архипелага придумали новый способ сравнения строк. Две строки считаются равными, если символы одной
из них можно заменить на символы другой так, что первая строка станет точной копией второй строки. При этом необходимо
соблюдение двух условий:

Порядок вхождения символов должен быть сохранён.
Одинаковым символам первой строки должны соответствовать одинаковые символы второй строки. Разным символам —– разные.
Например, если строка s = «abacaba», то ей будет равна строка t = «xhxixhx», так как все вхождения «a» заменены на «x»,
«b» –— на «h», а «c» –— на «i». Если же первая строка s=«abc», а вторая t=«aaa», то строки уже не будут равны, так как
разные буквы первой строки соответствуют одинаковым буквам второй.

Формат ввода
В первой строке записана строка s, во второй –— строка t. Длины обеих строк не превосходят 106. Обе строки содержат
хотя бы по одному символу и состоят только из маленьких латинских букв.

Строки могут быть разной длины.

Формат вывода
Выведите «YES», если строки равны (согласно вышеописанным правилам), и «NO» в ином случае.
"""

import sys


def hash_mask(seq):
    hash_map = {}
    next_digit = 0
    res = []

    for s in seq:
        if s not in hash_map:
            hash_map[s] = next_digit
            next_digit += 1
        res.append(hash_map[s])

    return res


def main():
    seq1 = sys.stdin.readline().rstrip()
    seq2 = sys.stdin.readline().rstrip()

    hash1 = hash_mask(seq1)
    hash2 = hash_mask(seq2)

    if hash1 == hash2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
