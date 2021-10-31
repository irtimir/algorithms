from node import Node


def insert(root, key):
    if key < root.value:
        if root.left is None:
            root.left = Node(None, None, key)
        else:
            insert(root.left, key)
    if key >= root.value:
        if root.right is None:
            root.right = Node(None, None, key)
        else:
            insert(root.right, key)
    return root
