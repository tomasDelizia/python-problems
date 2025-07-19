def top_k_frequent(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    frequencies = {}
    for num in nums:
        frequencies[num] = 1 + frequencies.get(num, 0)

    values_per_count = [[] for i in range(n + 1)]
    max_count = 0
    for num, count in frequencies.items():
        values_per_count[count].append(num)
        max_count = max(max_count, count)

    result = []
    # We ignore the index 0 and all the count indices that are empty
    for count in range(max_count, 1, -1):
        for num in values_per_count[count]:
            if len(result) == k:
                break
            result.append(num)

    return result
