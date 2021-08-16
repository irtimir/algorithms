"""
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно популярная.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:

пустая строка —– правильная скобочная последовательность;
правильная скобочная последовательность, взятая в скобки одного типа, –— правильная скобочная последовательность;
правильная скобочная последовательность с приписанной слева или справа правильной скобочной
последовательностью —– тоже правильная.
На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True,
если последовательность правильная, а иначе False.

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.
"""

import sys

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def is_correct_bracket_seq(seq):
    stack = Stack()
    for s in seq:
        if s in PAIRS:
            stack.push(s)
        else:
            try:
                element = stack.pop()
            except IndexError:
                return False
            if s != PAIRS[element]:
                return False

    return False if stack.size() else True


def main():
    seq = sys.stdin.readline().rstrip()
    print(is_correct_bracket_seq(seq))


if __name__ == '__main__':
    main()
