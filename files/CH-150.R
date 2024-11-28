library(tidyverse)

solve_n_queens_fixed = function(n, first_queen) {
  col_names = LETTERS[1:n]
  first_col = match(substr(first_queen, 1, 1), col_names)
  first_row = n + 1 - as.numeric(substr(first_queen, 2, 2))
  
  queens = integer(n)
  queens[first_col] = first_row
  
  is_safe = function(queens, row, col) {
    cols_with_queens = which(queens > 0)
    rows_with_queens = queens[cols_with_queens]
    all(row != rows_with_queens & abs(row - rows_with_queens) != abs(col - cols_with_queens))
  }
  
  place_queens = function(queens, col) {
    if (col > n) return(list(queens))
    if (queens[col] > 0) return(place_queens(queens, col + 1))
    
    1:n %>%
      keep(~ is_safe(queens, .x, col)) %>%
      map(~ {
        queens[col] = .x
        solutions = place_queens(queens, col + 1)
        queens[col] = 0
        solutions
      }) %>%
      flatten()
  }
  
  solutions = place_queens(queens, 1) %>% keep(~ all(.x > 0))
  solutions
}

solutions = solve_n_queens_fixed(8, "F8")

print_solution = function(solution) {
  n = length(solution)
  board = matrix(".", n, n)
  walk2(solution, 1:n, ~ { board[.x, .y] <<- "Q" })
  board = board[n:1, ]
  apply(board, 1, paste, collapse = " ") %>% walk(cat, "\n")
  cat("\n")
}

solutions %>% walk(print_solution)
