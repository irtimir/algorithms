"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения максимума среди элементов в стеке.
Сложность операции должна быть O(1). Для пустого стека операция должна возвращать None.
При этом push(x) и pop() также должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 100000.
Далее идут команды по одной в строке. Команды могут быть следующих видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды pop — «error».
"""

import sys


class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_history = []

    def push(self, item):
        self.items.append(item)

        if len(self.items) == 1:
            self.max_history.append(item)
            return

        if item > self.max_history[-1]:
            self.max_history.append(item)
        else:
            self.max_history.append(self.max_history[-1])

    def pop(self):
        self.max_history.pop()
        return self.items.pop()

    def get_max(self):
        return self.max_history[-1]


def handle_stack_commands(commands):
    stack = StackMaxEffective()
    for command in commands:
        if command.startswith('get_max'):
            try:
                print(stack.get_max())
            except IndexError:
                print(None)
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
