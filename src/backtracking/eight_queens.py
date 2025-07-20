def eight_queens() -> bool:
    row_on_col = [-1 for _ in range(8)]
    row_free = [True for _ in range(8)]
    inverse_diagonal_free = [True for _ in range(15)]
    normal_diagonal_free = [True for _ in range(15)]

    def place_queen(col: int) -> bool:
        print(f"Placing queen in column {col}")
        result = False
        for row in range(8):
            if result:
                break
            id = col + row
            nd = col - row + 7
            if (
                row_free[row]
                and inverse_diagonal_free[id]
                and normal_diagonal_free[nd]
            ):
                row_on_col[col] = row
                row_free[row] = inverse_diagonal_free[id] = (
                    normal_diagonal_free[nd]
                ) = False
                if col == 7:
                    result = True
                    break
                # Intend on next column
                result = place_queen(col + 1)
                if not result:
                    # Backtrack
                    row_free[row] = True
                    inverse_diagonal_free[id] = True
                    normal_diagonal_free[nd] = True
        return result

    result = place_queen(0)
    if not result:
        print("No solution found")
    else:
        print("Solution found")
        print("Row on column:", row_on_col)
        print_board(row_on_col)
    return result


def print_board(row_on_col: list[int]) -> None:
    for row in range(8):
        for col in range(8):
            if row_on_col[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
