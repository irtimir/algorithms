"""
Run id: 52516926

-- ПРИНЦИП РАБОТЫ --
Подобно бинарному поиску, делим последовательность на 2 части: "корректно" отстортированную и "сломанную", проверяем,
может ли искомое значение находиться в "корректно" отсортированной части, если явно нет, то выбираем для поиска
"сломанную" часть и рекурсивно вызываем поиск в выбранной части последовательности

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
За основу алгоритма взят классический бинарный поиск к небольшими доработками в условии, что если искомое значение
явно не находится между границами подпоследовательности, то, возможно, оно может находиться в "сломанной" части
последовательности, потому что явные предельные значения последовательноссти неизвестны.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Подобно классическому бинарному поиску в упорядоченном списке, происходит деление массива на 2 части по среднему
индексу, таким образом, сложность сохраняется и явряется O(logN).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Оперативная память используется только для хранения элементов исходного массива, поэтому алгоритм будет
потреблять O(N) памяти.
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
