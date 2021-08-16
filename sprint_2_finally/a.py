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

Run ID: 52356209
"""

"""
Run ID: 52356209

-- ПРИНЦИП РАБОТЫ --
За основу структуры Дек взят кольцевой буфер. 
У дека есть 2 указателя: `head` - указатель для записи в начало и `tail` - указатель для записи в конец.
При вставке элемента происходит проверка текущего размера Дека, если вставка возможна, элемент 
записывается на соответвующий индекс head/tail и просходит смещение указателя для записи следующего 
элемента: для `head` -1, для `tail` +1.
При извлечении элемента происходит указатель смещается для `head` +1, для `tail` -1, по полученному 
индексу будет возвращён элемент, а его место освободится для записи.

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
        self.max_size = max_size
        self.items = [None] * max_size
        self.size = 0
        self.head = max_size - 1
        self.tail = 0

    def push_back(self, value):
        if self.size == self.max_size:
            raise StackOverflow('list overflow')

        self.items[self.tail] = value
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, value):
        if self.size == self.max_size:
            raise StackOverflow('list overflow')

        self.items[self.head] = value
        self.head = (self.head - 1) % self.max_size
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            raise IndexError('pop from empty list')
        self.head = (self.head + 1) % self.max_size
        elem = self.items[self.head]
        self.items[self.head] = None
        self.size -= 1
        return elem

    def pop_back(self):
        if self.size == 0:
            raise IndexError('pop from empty list')
        self.tail = (self.tail - 1) % self.max_size
        elem = self.items[self.tail]
        self.items[self.tail] = None
        self.size -= 1
        return elem


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
