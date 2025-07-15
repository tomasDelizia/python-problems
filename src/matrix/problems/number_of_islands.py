from collections import deque

directions = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, -1),  # Left
    (0, 1),  # Right
]


def number_of_islands(grid: list[list[str]]) -> int:
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    count = 0
    visited: set[tuple[int, int]] = set()

    def bfs_island(r: int, c: int) -> None:
        queue = deque()
        queue.append((r, c))
        visited.add((r, c))
        while queue:
            r, c = queue.popleft()
            for dx, dy in directions:
                is_land_cell = (
                    r + dx in range(rows)
                    and c + dy in range(cols)
                    and grid[r + dx][c + dy] == "1"
                    and (r + dx, c + dy) not in visited
                )
                if not is_land_cell:
                    continue
                visited.add((r + dx, c + dy))
                queue.append((r + dx, c + dy))

    for r in range(rows):
        for c in range(cols):
            current = grid[r][c]
            if current == "0" or (r, c) in visited:
                continue
            bfs_island(r, c)
            count += 1
    return count
