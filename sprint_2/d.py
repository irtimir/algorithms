"""
Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите функцию solution,
определяющую индекс первого вхождения передаваемого ей на вход значения в связном списке, если значение присутствует.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def find_element(node, value):
    match = None
    counter = 0
    while match is None and node is not None:
        if node.value == value:
            return counter
        counter += 1
        node = node.next_item

    return -1


def solution(node, elem):
    return find_element(node, elem)


def test():
    node3 = Node('node3', None)
    node2 = Node('node2', node3)
    node1 = Node('node1', node2)
    node0 = Node('node0', node1)
    assert -1 == solution(node0, 'node21')
    # result is idx == 2

if __name__ == '__main__':
    test()
