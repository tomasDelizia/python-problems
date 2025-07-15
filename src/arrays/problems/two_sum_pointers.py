def two_sum_pointers(arr: list[int], target: int):
    """
    Find two indices in a sorted array such that their values sum to the
    target.
    """
    left, right = 0, len(arr) - 1
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        if sum > target:
            right -= 1
        else:
            left += 1
    return []
