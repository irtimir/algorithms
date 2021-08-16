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
    return rm_element(node, idx)
