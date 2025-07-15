from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows, cols = len(board), len(board[0])
    if rows != 9 or cols != 9:
        return False

    seen_per_row = defaultdict(set)
    seen_per_col = defaultdict(set)
    seen_per_box = defaultdict(set)

    for r in range(9):
        for c in range(9):
            current = board[r][c]
            if current == ".":
                continue
            box_key = (r // 3, c // 3)
            if (
                current in seen_per_row[r]
                or current in seen_per_col[c]
                or current in seen_per_box[box_key]
            ):
                return False
            seen_per_row[r].add(current)
            seen_per_col[c].add(current)
            seen_per_box[box_key].add(current)
    return True
