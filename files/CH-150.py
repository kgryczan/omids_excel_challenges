import numpy as np

def solve_n_queens_fixed(n, first_queen):
    col_names = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[:n]
    first_col = col_names.index(first_queen[0])
    first_row = n - int(first_queen[1])

    queens = np.zeros(n, dtype=int)
    queens[first_col] = first_row + 1

    def is_safe(queens, row, col):
        cols_with_queens = np.where(queens > 0)[0]
        rows_with_queens = queens[cols_with_queens] - 1
        return all(row != rows_with_queens) and all(abs(row - rows_with_queens) != abs(col - cols_with_queens))

    def place_queens(queens, col):
        if col >= n:
            return [queens.copy()]
        if queens[col] > 0:
            return place_queens(queens, col + 1)

        solutions = []
        for row in range(n):
            if is_safe(queens, row, col):
                queens[col] = row + 1
                solutions.extend(place_queens(queens, col + 1))
                queens[col] = 0
        return solutions

    solutions = [sol for sol in place_queens(queens, 0) if all(sol > 0)]
    return solutions

def print_solution(solution):
    n = len(solution)
    board = np.full((n, n), ".")
    for col, row in enumerate(solution):
        board[n - row, col] = "Q"
    for row in board:
        print(" ".join(row))
    print()

solutions = solve_n_queens_fixed(8, "F8")
for sol in solutions:
    print_solution(sol)