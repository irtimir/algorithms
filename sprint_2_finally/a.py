"""
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много
элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1).
Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации нельзя использовать связный список.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 5000. Во второй строке записано
число m — максимальный размер дека. Он не превосходит 1000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.

Run ID: 52362847
"""

"""
Run ID: 52362847

-- ПРИНЦИП РАБОТЫ --
За основу структуры Дек взят кольцевой буфер. 
У дека есть 2 указателя: `head` - указатель первого элемента и `tail` - указатель последнего элемента.
При вставке элемента происходит проверка текущего размера Дека, если вставка возможна, элемент 
записывается на соответвующий индекс (head - 1)/(tail + 1).
При извлечении элемента, происходит получение элемента по индексу head/tail и последующее смещение 
указателя на (head + 1)/(tail - 1).

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Кольцевой буфер - это очередь ограниченного размера, таким образом Дек не выйдет за пределы максимального размера.
Очереди сохраняют порядок элементов, поэтому извлекаться и добавляться элементы в Дек будут поледовательно, 
друг за другом. Методы `_back`/`_front` инвертируют друг друга относительно стороны очереди, 
поэтому Дек является двусторонней очередью.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление в Дек стоит O(1), потому что добаление в очередь стоит O(1)
Извлечение из Дека стоит O(1), потому что получение элемента по индексу и запись по индексу стоит O(1)
Таким образом любая опарация над Деком имеет сложность O(1).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Если Дек масимальной длины n элементов, то кольцевой буфер будет сожержать n элементов.
Таким образом Дек будет потреблять O(N) памяти.
"""

import sys


class StackOverflow(Exception):
    pass


class Deque:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.head = None
        self.tail = None

    def get_size(self):
        if self.head is None and self.tail is None:
            return 0
        elif self.head == self.tail:
            return 1
        elif self.tail < self.head:
            return (self.tail + (self.get_max_size() - 1 - self.head)) + 2
        else:
            return abs((self.head - self.tail + 1) - 2)

    def get_max_size(self):
        return len(self.items)

    def push_back(self, value):
        size = self.get_size()
        if size == self.get_max_size():
            raise StackOverflow('list overflow')

        if size == 0:
            self.tail = self.head = 0
        else:
            self.tail = self._move_pointer(self.tail, 1)

        self.items[self.tail] = value

    def push_front(self, value):
        size = self.get_size()
        if size == self.get_max_size():
            raise StackOverflow('list overflow')
        if size == 0:
            self.tail = self.head = 0
        else:
            self.head = self._move_pointer(self.head, -1)
        self.items[self.head] = value

    def pop_front(self):
        if self.get_size() == 0:
            raise IndexError('pop from empty list')
        elem = self.items[self.head]
        self.items[self.head] = None

        if self.head == self.tail:
            self.tail = self.head = None
        else:
            self.head = self._move_pointer(self.head, 1)
        return elem

    def pop_back(self):
        if self.get_size() == 0:
            raise IndexError('pop from empty list')
        elem = self.items[self.tail]
        self.items[self.tail] = None
        if self.head == self.tail:
            self.tail = self.head = None
        else:
            self.tail = self._move_pointer(self.tail, -1)
        return elem

    def _move_pointer(self, pointer_value, value):
        return (pointer_value + value) % self.get_max_size()


def handle_command(deque, command):
    if command.startswith('push_front'):
        try:
            deque.push_front(command.split()[1])
        except StackOverflow:
            print('error')
    elif command.startswith('push_back'):
        try:
            deque.push_back(command.split()[1])
        except StackOverflow:
            print('error')
    elif command.startswith('pop_front'):
        try:
            print(deque.pop_front())
        except IndexError:
            print('error')
    elif command.startswith('pop_back'):
        try:
            print(deque.pop_back())
        except IndexError:
            print('error')


def main():
    commands_num = int(sys.stdin.readline().rstrip())
    deque_max_size = int(sys.stdin.readline().rstrip())

    deque = Deque(deque_max_size)

    for _ in range(commands_num):
        handle_command(deque, sys.stdin.readline().rstrip())


if __name__ == '__main__':
    main()
