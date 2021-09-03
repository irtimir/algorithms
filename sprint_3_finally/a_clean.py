"""
Run id: 52516926
"""


def search_in_interval(nums, target, left, right) -> int:
    if right - left == 1:
        if nums[left] == target:
            return left
        return -1
    elif right - left == 2:
        if nums[left] == target:
            return left
        if nums[right - 1] == target:
            return right - 1
        return -1
    else:
        mid = left + (right - left) // 2

        if nums[left] <= target <= nums[mid - 1]:
            return search_in_interval(nums, target, left, mid)
        elif nums[mid] <= target <= nums[right - 1]:
            return search_in_interval(nums, target, mid, right)
        elif nums[left] > nums[mid - 1]:
            return search_in_interval(nums, target, left, mid)
        else:
            return search_in_interval(nums, target, mid, right)


def broken_search(nums, target) -> int:
    return search_in_interval(nums, target, 0, len(nums))
