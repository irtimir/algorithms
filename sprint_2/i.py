"""
Астрологи объявили день очередей ограниченного размера. Тимофею нужно написать класс MyQueueSized,
который принимает параметр max_size, означающий максимально допустимое количество элементов в очереди.

Помогите ему —– реализуйте программу, которая будет эмулировать работу такой очереди. Функции,
которые надо поддержать, описаны в формате ввода.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 5000.
Во второй строке задан максимально допустимый размер очереди, он не превосходит 5000.
Далее идут команды по одной на строке. Команды могут быть следующих видов:

push(x) — добавить число x в очередь;
pop() — удалить число из очереди и вывести на печать;
peek() — напечатать первое число в очереди;
size() — вернуть размер очереди;
При превышении допустимого размера очереди нужно вывести «error». При вызове операций pop() или peek()
для пустой очереди нужно вывести «None».
"""

import sys


class MyQueueSized:
    def __init__(self, max_size):
        self.max_n = max_size
        self.size = 0
        self.items = [None] * self.max_n
        self.head = 0
        self.tail = 0

    def push(self, item):
        if self.size != self.max_n:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return True
        return False

    def pop(self):
        if self.size == 0:
            return
        elem = self.items[self.head]
        self.items[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return elem

    def peek(self):
        return self.items[self.head]


def handle_command(queue, command):
    if command.startswith('size'):
        print(queue.size)
    if command.startswith('peek'):
        print(queue.peek())
    elif command.startswith('push'):
        if not queue.push(command.split()[1]):
            print('error')
    elif command.startswith('pop'):
        print(queue.pop())


def main():
    commands_num = int(sys.stdin.readline().rstrip())

    max_size = int(sys.stdin.readline().rstrip())

    queue = MyQueueSized(max_size)

    for _ in range(commands_num):
        handle_command(queue, sys.stdin.readline().rstrip())


if __name__ == '__main__':
    main()
