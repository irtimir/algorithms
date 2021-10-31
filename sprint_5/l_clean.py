def sift_down(heap, idx):
    left = 2 * idx
    right = left + 1

    last_idx = len(heap) - 1

    if last_idx < left:
        return idx

    if right <= last_idx and heap[left] < heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    return idx
