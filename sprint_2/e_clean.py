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
