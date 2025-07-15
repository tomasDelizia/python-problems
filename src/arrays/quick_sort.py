def quick_sort(arr: list[int]):
    """
    Sorts an array using the Quick Sort algorithm.
    :param arr: list[int] - The list of integers to be sorted.
    """
    n = len(arr)
    if n <= 1:
        return
    left, right = 0, len(arr) - 1
    quick(arr, left, right)


def quick(arr: list[int], left: int, right: int):
    pivot = get_pivot(arr, left, right)
    i, j = left, right
    while i <= j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    if j > left:
        quick(arr, left, j)
    if i < right:
        quick(arr, i, right)


def get_pivot(arr: list[int], left: int, right: int) -> int:
    center = (left + right) // 2
    if arr[right] < arr[left]:
        arr[right], arr[left] = arr[left], arr[right]
    if arr[center] < arr[left]:
        arr[center], arr[left] = arr[left], arr[center]
    if arr[right] < arr[center]:
        arr[right], arr[center] = arr[center], arr[right]
    return arr[center]
