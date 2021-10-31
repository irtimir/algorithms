def sift_up(heap, idx):
    if idx == 1:
        return idx

    parent_index = idx // 2

    if heap[parent_index] < heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        return sift_up(heap, parent_index)

    return idx
