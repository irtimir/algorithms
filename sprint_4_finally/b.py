"""
B. Хеш-таблица
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	5 секунд	64Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Node.js 14.15.5	5 секунд	256Mb
Python 3.7.3	15 секунд	64Mb
Oracle Java 8	5 секунд	400Mb
OpenJDK Java 11	5 секунд	400Mb
Node JS 8.16	5 секунд	256Mb
Тимофей, как хороший руководитель, хранит информацию о зарплатах своих сотрудников в базе данных и постоянно её
обновляет. Он поручил вам написать реализацию хеш-таблицы, чтобы хранить в ней базу данных с зарплатами сотрудников.

Хеш-таблица должна поддерживать следующие операции:

put key value —– добавление пары ключ-значение. Если заданный ключ уже есть в таблице, то соответствующее ему значение
обновляется.
get key –— получение значения по ключу. Если ключа нет в таблице, то вывести «None». Иначе вывести найденное значение.
delete key –— удаление ключа из таблицы. Если такого ключа нет, то вывести «None», иначе вывести хранимое по данному
ключу значение и удалить ключ.
В таблице хранятся уникальные ключи.

Требования к реализации:

Нельзя использовать имеющиеся в языках программирования реализации хеш-таблиц (std::unordered_map в С++, dict в Python,
HashMap в Java, и т. д.)
Число хранимых в таблице ключей не превосходит 105.
Разрешать коллизии следует с помощью метода цепочек или с помощью открытой адресации.
Все операции должны выполняться за O(1) в среднем.
Поддерживать рехеширование и масштабирование хеш-таблицы не требуется.
Ключи и значения, id сотрудников и их зарплата, —– целые числа. Поддерживать произвольные хешируемые типы не требуется.
Формат ввода
В первой строке задано общее число запросов к таблице n (1≤ n≤ 106).

В следующих n строках записаны запросы, которые бывают трех видов –— get, put, delete —– как описано в условии.

Все ключи и значения –— целые неотрицательные числа, не превосходящие 109.

Формат вывода
На каждый запрос вида get и delete выведите ответ на него в отдельной строке.
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

    if chain_element is None:
        hash_table[hash_key] = ChainElement((key, value))
    else:
        while True:
            k, v = chain_element.value
            if key == k:
                chain_element.value = (key, value)
                break
            if chain_element.next is None:
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
            if prev_element is None:
                hash_table[hash_key] = None
            else:
                prev_element.next = chain_element.next
            return v
        prev_element = chain_element
        chain_element = chain_element.next


def main():
    hash_table = [None for _ in range(96557)]

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
