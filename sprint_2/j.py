"""
Любимый вариант очереди Тимофея — очередь, написанная с использованием связного списка.
Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если очередь пуста, то вывести «error».
put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 1000.
В каждой из следующих n строк записаны команды по одной строке.
"""

import sys


class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self):
        if self.head:
            elem = self.head.value
            self.head = self.head.next_item
            self.size -= 1
            if self.head is None:
                self.tail = None

            return elem

    def put(self, value):
        n = Node(value)
        if self.tail:
            self.tail.next_item = n
        else:
            self.head = n
        self.tail = n
        self.size += 1


def handle_command(queue, command):
    if command.startswith('size'):
        print(queue.size)
    elif command.startswith('put'):
        queue.put(command.split()[1])
    elif command.startswith('get'):
        if queue.size == 0:
            print('error')
        else:
            print(queue.get())


def main():
    commands_num = int(sys.stdin.readline().rstrip())
    queue = QueueLinkedList()

    for _ in range(commands_num):
        handle_command(queue, sys.stdin.readline().rstrip())


if __name__ == '__main__':
    main()
