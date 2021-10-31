"""
Run id: 54508674

-- ПРИНЦИП РАБОТЫ --
1. Создаём бинарную кучу
2. Вставляем все элементы входного в бинарную кучу
3. Создаём новый массив и заполняем его элементами получая из бинарной кучи самый приоритетный элемент

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Свойства бинарной кучи определяют, что значение родителя будут более приоритетны, чем в потомках, таким образом получая
элементы по одному с вершины кучи мы гарантируем корректность сортировки

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Создание кучи O(1)
Вставка элементов в кучу O(n log n)
Извлечение элементов из кучи O(n log n)
Таким образом O(1) + O(n log n) + O(n log n) = O(n log n)
В худшем случае будет работать за O(n log n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Хранение кучи - копия значений массива O(n)
Формирование отсортированного массива - копия значений из кучи O(n)
Таким образом сложность будет O(n) + O(n) = O(n)
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
