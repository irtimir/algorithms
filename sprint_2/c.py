"""
Вася размышляет, что ему можно не делать из того списка дел, который он составил.
Но, кажется, все пункты очень важные! Вася решает загадать число и удалить дело, которое идёт под этим номером.
Список дел представлен в виде односвязного списка. Напишите функцию solution, которая принимает на вход
голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
"""


# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def print_linked_list(node):
    while node is not None:
        print(node.value)
        node = node.next_item


def rm_element(node, idx):
    head = node
    prev_node = None

    for n in range(idx + 1):
        next_node = node.next_item

        if n == idx:
            if prev_node is None:
                return node.next_item
            prev_node.next_item = next_node
            return head

        prev_node = node
        node = node.next_item


def solution(node, idx):
    node = rm_element(node, idx)
    print_linked_list(node)
    return node


def test():
    node3 = Node('node3', None)
    node2 = Node('node2', node3)
    node1 = Node('node1', node2)
    node0 = Node('node0', node1)
    new_head = solution(node0, 3)
    print_linked_list(new_head)
    # result is node0 -> node2 -> node3


def main():
    test()

if __name__ == '__main__':
    main()
