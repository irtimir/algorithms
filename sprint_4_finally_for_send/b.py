"""
Run id: 53505723

-- ПРИНЦИП РАБОТЫ --
За основу хеш-таблицы взята структура данных - list, который изначально заполнен значениями None. Корзина реализована
как ссылка на голову односвязного списка, в котором находятся элементы.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Размер хеша определяет простое число, таким образом увлечивается вероятность равномерного распреления элементов по
хеш-таблице.
Добавление элемента происходит посредством вычисления номера корзины и проход по односвязному списку с целью проверки
существования вставляемого ключа, если ключ не найден, объект помещается в конец списка.
Получение элемента происходит посредством вычисления номера корзины и дальнейшим проходом по односвязному списку.
Удаление элемента происходит посредством вычисления номера корзины и дальнейшим проходом по односвязному списку и
удалением элемента из односвязного списка.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
При правильно подобранном размере хеш-таблицы, каждая операция будет занимать около O(1) времени.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Хранятся только элементы, которые добавлены в хеш-таблицу, таким бразом используется O(N) памяти.
"""

import sys


class ChainElement:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item


def get_hash_key(hash_table, key):
    return key % len(hash_table)


def insert(hash_table, key, value):
    hash_key = get_hash_key(hash_table, key)
    chain_element = hash_table[hash_key]

    if not chain_element:
        hash_table[hash_key] = ChainElement((key, value))
    else:
        while True:
            k, v = chain_element.value
            if key == k:
                chain_element.value = (key, value)
                break
            if not chain_element.next:
                chain_element.next = ChainElement((key, value))
                break
            chain_element = chain_element.next


def get(hash_table, key):
    hash_key = get_hash_key(hash_table, key)
    chain_element = hash_table[hash_key]

    while chain_element:
        k, v = chain_element.value
        if key == k:
            return v
        chain_element = chain_element.next


def delete(hash_table, key):
    hash_key = get_hash_key(hash_table, key)
    prev_element = None
    chain_element = hash_table[hash_key]

    while chain_element:
        k, v = chain_element.value
        if key == k:
            if not prev_element:
                hash_table[hash_key] = None
            else:
                prev_element.next = chain_element.next
            return v
        prev_element = chain_element
        chain_element = chain_element.next


def main():
    hash_table_size = 96557
    hash_table = [None for _ in range(hash_table_size)]

    for _ in range(int(sys.stdin.readline().rstrip())):
        command = sys.stdin.readline().rstrip()

        if command.startswith('put'):
            _, key, value = command.split()
            insert(hash_table, int(key), int(value))
        elif command.startswith('get'):
            _, key = command.split()
            print(get(hash_table, int(key)))
        elif command.startswith('delete'):
            _, key = command.split()
            print(delete(hash_table, int(key)))


if __name__ == '__main__':
    main()
