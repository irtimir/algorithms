def merge(arr, lf, mid, rg):
    l, r = lf, mid

    merged = []

    while l < mid and r < rg:
        if arr[l] <= arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1

    for i in range(l, mid):
        merged.append(arr[i])

    for i in range(r, rg):
        merged.append(arr[i])

    return merged


def merge_sort(arr, lf, rg):
    if rg - lf == 1:
        pass
    elif rg - lf == 2:
        if arr[lf] > arr[rg - 1]:
            arr[lf], arr[rg - 1] = arr[rg - 1], arr[lf]
    else:
        mid = lf + (rg - lf) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)

        tmp = merge(arr, lf, mid, rg)

        for i in range(lf, rg):
            arr[i] = tmp[i - lf]
