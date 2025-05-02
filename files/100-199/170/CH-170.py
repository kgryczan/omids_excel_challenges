def knights_tour(N, start_pos):
    board = [[-1] * N for _ in range(N)]
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    def pos_to_indices(pos):
        return N - int(pos[1:]), ord(pos[0].lower()) - ord('a')
    
    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < N and board[x][y] == -1
    
    def count_onward_moves(x, y):
        return sum(is_valid(x + dx, y + dy) for dx, dy in moves)
    
    def solve(x, y, step):
        board[x][y] = step
        if step == N * N - 1:
            return True
        possible_moves = sorted(((count_onward_moves(x + dx, y + dy), x + dx, y + dy) for dx, dy in moves if is_valid(x + dx, y + dy)), key=lambda x: x[0])
        for _, nx, ny in possible_moves:
            if solve(nx, ny, step + 1):
                return True
        board[x][y] = -1
        return False
    
    start_row, start_col = pos_to_indices(start_pos)
    if not solve(start_row, start_col, 0):
        print("No solution exists for the given board and starting position.")
        return

    for row in board:
        print(' '.join(f"{cell:2}" for cell in row))

if __name__ == "__main__":
    knights_tour(8, 'a8')
