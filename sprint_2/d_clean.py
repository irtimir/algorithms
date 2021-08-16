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
