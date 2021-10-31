"""
A. Пирамидальная сортировка
Язык	Ограничение времени	Ограничение памяти	Ввод	Вывод
Все языки	5 секунд	256Mb	стандартный ввод или input.txt	стандартный вывод или output.txt
Oracle Java 8	1.5 секунд	256Mb
OpenJDK Java 11	1.5 секунд	256Mb
GNU c++17 7.3	0.7 секунд	64Mb
В данной задаче необходимо реализовать сортировку кучей. При этом кучу необходимо реализовать самостоятельно,
использовать имеющиеся в языке реализации нельзя. Сначала рекомендуется решить задачи про просеивание вниз и вверх.

Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров.
Задачи подобраны, участники зарегистрированы, тесты написаны. Осталось придумать, как в конце соревнования будет
определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему будут привязаны два показателя:
количество решённых задач Pi и размер штрафа Fi. Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот,
у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом. Если же
и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин. В своё отсутствие он поручил вам
реализовать алгоритм сортировки кучей (англ. Heapsort) для таблицы результатов.

Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:

уникальным логином (строкой из маленьких латинских букв длиной не более 20)
числом решённых задач Pi
штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.
Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному в строке.
"""

import sys
from collections import namedtuple

ResultSortKey = namedtuple('ResultSortKey', ['done', 'fine', 'username'])


def sift_down(heap, idx):
    left = 2 * idx
    right = left + 1

    last_idx = len(heap) - 1

    if last_idx < left:
        return idx

    if right <= last_idx and heap[left] > heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[idx] > heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    return idx


def sift_up(heap, idx):
    if idx == 1:
        return idx

    parent_index = idx // 2

    if heap[parent_index] > heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        return sift_up(heap, parent_index)

    return idx


def heap_add(heap, key):
    new_idx = len(heap)
    heap.append(key)
    sift_up(heap, new_idx)


def pop_max(heap):
    result = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 1)
    return result


def heapsort(array):
    heap = [-1]

    for item in array:
        heap_add(heap, item)

    sorted_array = []
    while len(heap) > 1:
        sorted_array.append(pop_max(heap))

    return sorted_array


def main():
    results = []
    for i in range(int(sys.stdin.readline().rstrip())):
        username, done, fine = sys.stdin.readline().rstrip().split()
        results.append(ResultSortKey(done=-int(done), fine=int(fine), username=username))
    print(*map(lambda result: result.username, heapsort(results)), sep='\n')


if __name__ == '__main__':
    main()
