def solution(root) -> bool:
    if root.left:
        if root.left.value >= root.value or not solution(root.left):
            return False

    if root.right:
        if root.right.value <= root.value or not solution(root.right):
            return False
    return True
