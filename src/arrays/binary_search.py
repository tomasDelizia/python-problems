def binary_search(arr: list[int], target: int) -> int:
    """
    Perform binary search on a sorted array to find the index of the target value.

    :param arr: List[int] - A sorted list of integers.
    :param target: int - The integer value to search for.
    :return: int - The index of the target in the array, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
