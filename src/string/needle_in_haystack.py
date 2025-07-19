def needle_in_haystack(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0
    if n < m:
        return -1
    for i in range(0, n - m + 1):
        if haystack[i : i + m] == needle:
            return i
    return -1
