def solution(node):
    while node is not None:
        print(node.value)
        node = node.next_item
