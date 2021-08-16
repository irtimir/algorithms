"""
Вася решил запутать маму —– делать дела в обратном порядке. Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.
"""


# Comment it before submitting
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def print_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next


def reverse_nodes(node):
    while True:
        next_node = node.next
        node.next, node.prev = node.prev, node.next
        if next_node is not None:
            node = next_node
        else:
            return node


def solution(node):
    return reverse_nodes(node)


def test():
    node3 = DoubleConnectedNode('node3')
    node2 = DoubleConnectedNode('node2')
    node1 = DoubleConnectedNode('node1')
    node0 = DoubleConnectedNode('node0')

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)

    print(new_head.value)
    print_linked_list(new_head)
    # print(new_head)
    # result is new_head == node3
    # node3.next == node2
    # node2.next == node1 node2.prev == node3
    # node1.next == node0 node1.prev == node2
    # node0.prev == node1


if __name__ == '__main__':
    test()
