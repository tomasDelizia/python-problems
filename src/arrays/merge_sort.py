def merge_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n <= 1:
        return arr
    center = n // 2
    left_half = arr[:center]
    right_half = arr[center:]
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def merge(a: list[int], b: list[int]) -> list[int]:
    n, m = len(a), len(b)
    c = []
    i, j, k = 0, 0, 0
    while i < n and j < m:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
        k += 1
    while i < n:
        c.append(a[i])
        i += 1
    while j < m:
        c.append(b[j])
        j += 1
    return c
