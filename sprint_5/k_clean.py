def print_range(node, l, r):
    if node.left and node.value >= l:
        print_range(node.left, l, r)

    if l <= node.value <= r:
        print(node.value)

    if node.right and node.value <= r:
        print_range(node.right, l, r)
