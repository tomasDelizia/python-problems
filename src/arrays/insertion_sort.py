def insertion_sort(arr: list[int], h: int = 1):
    n = len(arr)
    if n <= 1:
        return
    for j in range(h, n):
        current = arr[j]
        k = j - h
        while k >= 0 and current < arr[k]:
            arr[k + h] = arr[k]
            k -= h
        arr[k + h] = current
