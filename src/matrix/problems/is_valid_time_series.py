def is_valid_time_series_brute(grid: list[list[int]]) -> bool:
    rows, cols = len(grid), len(grid[0])
    if rows < 2:
        return True
    for r in range(1, rows):
        for c in range(cols):
            current = grid[r][c]
            prev = grid[r - 1][c]
            if current != prev:
                # Validate first column
                if c == 0 and grid[r][1] == grid[r - 1][1]:
                    return False
                # Validate last column
                if (
                    c == cols - 1
                    and grid[r][cols - 2] == grid[r - 1][cols - 2]
                ):
                    return False
                # Validate middle columns
                if (
                    grid[r][c - 1] == grid[r - 1][c - 1]
                    and grid[r][c + 1] == grid[r - 1][c + 1]
                ):
                    return False
    return True


def is_valid_time_series(grid: list[list[int]]) -> bool:
    rows = len(grid)
    if rows < 2:
        return True

    def get_positions(row: list[int]):
        return [i for i, val in enumerate(row) if val == 1]

    previous_positions = get_positions(grid[0])

    for row in grid[1:]:
        current_positions = get_positions(row)
        if len(current_positions) != len(previous_positions):
            return False  # Robot count changed

        # Match current positions to previous ones in order
        for prev, curr in zip(
            sorted(previous_positions), sorted(current_positions)
        ):
            if abs(prev - curr) > 1:
                return False
        previous_positions = current_positions

    return True
