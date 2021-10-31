def solution(root):
    current_max = root.value
    if root.left:
        max_l = solution(root.left)
        if max_l > current_max:
            current_max = max_l
    if root.right:
        max_r = solution(root.right)
        if max_r > current_max:
            current_max = max_r
    return current_max
