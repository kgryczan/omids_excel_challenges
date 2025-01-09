knights_tour = function(N, start_pos) {
    board = matrix(-1, nrow = N, ncol = N)
    pos_to_indices = function(pos, N) {
        col_letter = toupper(substr(pos, 1, 1))
        row_number = as.numeric(substr(pos, 2, nchar(pos)))
        col = match(col_letter, LETTERS)
        row = N - row_number + 1
        return(list(row = row, col = col))
    }
    moves = list(
        c(-2, -1), c(-1, -2), c(1, -2), c(2, -1),
        c(2, 1), c(1, 2), c(-1, 2), c(-2, 1)
    )
    is_valid = function(x, y, board, N) {
        return(x >= 1 && x <= N && y >= 1 && y <= N && board[x, y] == -1)
    }
    count_onward_moves = function(x, y, board, N, moves) {
        sum(purrr::map_lgl(moves, function(move) is_valid(x + move[1], y + move[2], board, N)))
        }
    solve = function(x, y, step, board, N, moves) {
        board[x, y] = step
        
        if (step == N * N - 1) {
            return(board)
        }
        possible_moves = list()
        for (move in moves) {
            nx = x + move[1]
            ny = y + move[2]
            if (is_valid(nx, ny, board, N)) {
                c_moves = count_onward_moves(nx, ny, board, N, moves)
                possible_moves = append(possible_moves, list(c(c_moves, nx, ny)))
            }
        }
        if (length(possible_moves) == 0) {
            board[x, y] = -1
            return(NULL)
        }
        possible_moves = possible_moves[order(sapply(possible_moves, function(m) m[1]))]
        
        for (move in possible_moves) {
            next_step = solve(move[2], move[3], step + 1, board, N, moves)
            if (!is.null(next_step)) {
                return(next_step)
            }
        }=======
        board[x, y] = -1
        return(NULL)
    }
    indices = pos_to_indices(start_pos, N)
    start_row = indices$row
    start_col = indices$col
    if (is.na(start_col) || start_col < 1 || start_col > N ||
        start_row < 1 || start_row > N) {
        stop("Invalid starting position.")
    }
    result = solve(start_row, start_col, 0, board, N, moves)
    if (is.null(result)) {
        cat("No solution exists for the given board and starting position.\n")
        return(NULL)
    }
    format_board = function(board) {
        formatted = apply(board, 1, function(row) {
            paste(sprintf("%2d", row), collapse = " ")
        })
        return(paste(formatted, collapse = "\n"))
    }
    
    cat(format_board(result), "\n")
    return(result)
}

N = 8
start_position = 'a8'

a = data.frame(knights_tour(N, start_position))
