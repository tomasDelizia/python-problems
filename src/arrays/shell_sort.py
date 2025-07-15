from .insertion_sort import insertion_sort


def shell_sort(arr: list[int]):
    n = len(arr)
    if n <= 1:
        return
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        insertion_sort(arr, h)
        h //= 3
