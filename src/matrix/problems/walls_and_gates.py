directions = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, -1),  # Left
    (0, 1),  # Right
]

EMPTY, WALL, GATE = float("inf"), -1, 0


def walls_and_gates(grid):
    """
    Fills grid values that are empty with the steps required to get from that
    cell to the closest gate.
    Time complexity: O(n.m)
    Space complexity: O(n.m)
    """
    rows = len(grid)
    if rows == 0:
        return grid
    cols = len(grid[0])

    def dfs_gate(row, col, steps):
        # Only process valid values that aren't gates or walls and that are
        # less than the current recorded steps in that cell.
        if (
            row not in range(rows)
            or col not in range(cols)
            or grid[row][col] < steps
        ):
            return
        grid[row][col] = steps
        for dx, dy in directions:
            dfs_gate(row + dx, col + dy, steps + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == GATE:
                dfs_gate(r, c, 0)

    return grid
