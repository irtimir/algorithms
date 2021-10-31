def tree_height(root):
    if root.left is not None:
        left_height = tree_height(root.left)
    else:
        left_height = 0

    if root.right is not None:
        right_height = tree_height(root.right)
    else:
        right_height = 0

    if abs(right_height - left_height) > 1:
        raise ValueError()

    return 1 + max(left_height, right_height)


def solution(root):
    try:
        if root.left is not None:
            left_height = tree_height(root.left)
        else:
            left_height = 0

        if root.right is not None:
            right_height = tree_height(root.right)
        else:
            right_height = 0
        if abs(right_height - left_height) > 1:
            raise ValueError()
        return True
    except ValueError:
        return False
