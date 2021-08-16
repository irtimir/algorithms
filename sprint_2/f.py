"""
Нужно реализовать класс StackMax, который поддерживает операцию определения максимума среди всех элементов в стеке.
Класс должен поддерживать операции push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд, которое не превосходит 10000.
В следующих n строках идут команды. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None», для команды pop() — «error».
"""

import sys


class StackMax:
    def __init__(self):
        self.items = []
        self.max = None

    def push(self, item):
        if self.max is None or self.max < item:
            self.max = item
        self.items.append(item)

    def pop(self):
        elem = self.items.pop()

        if elem == self.max:
            self.max = None
            if self.items:
                self.max = max(self.items)
        return elem


def handle_stack_commands(commands):
    stack = StackMax()
    for command in commands:
        if command.startswith('get_max'):
            print(stack.max)
        elif command.startswith('push'):
            stack.push(int(command.split()[1]))
        elif command.startswith('pop'):
            try:
                stack.pop()
            except IndexError:
                print('error')


def main():
    commands_num = int(sys.stdin.readline().rstrip())

    commands = []

    for _ in range(commands_num):
        commands.append(sys.stdin.readline().rstrip())

    handle_stack_commands(commands)


if __name__ == '__main__':
    main()
