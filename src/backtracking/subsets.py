import copy


def subsets(nums: list[int]) -> list[list[int]]:
    result = [[]]  # Include the empty subset

    def recurse(index: int, arr: list[int]) -> None:
        for i in range(index, len(nums)):
            arr.append(nums[i])
            result.append(copy.copy(arr))  # Append copy of arr
            recurse(i + 1, arr)
            arr.pop()

    recurse(0, [])
    return result
