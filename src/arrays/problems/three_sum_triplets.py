def three_sum_triplets(arr: list[int], target: int) -> list[tuple[int]]:
    result = []
    arr.sort()
    n = len(arr)
    for i in range(n):
        a = arr[i]
        # Avoid reusing the same value.
        if i > 0 and a == arr[i - 1]:
            continue
        # Do two sum.
        left, right = i + 1, n - 1
        while left < right:
            threeSum = a + arr[left] + arr[right]
            if threeSum == target:
                triplet = (a, arr[left], arr[right])
                if triplet not in result:
                    result.append(triplet)
                # Update one of the pointers.
                left += 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
            elif threeSum > target:
                right -= 1
            else:
                left += 1
    return result
