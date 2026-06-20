library(tidyverse)
library(readxl)
path <- "400-499/430/CH-430 - Knight Distance Problem.xlsx"
start <- "a2"
input <- read_excel(path, range = "L3:L6")
test <- read_excel(path, range = "M3:M6") %>%
  mutate(Path = str_replace_all(Path, " ", ""))

blocked <- expand_grid(file = letters[3:4], rank = 1:6) |>
  transmute(cell = str_c(file, rank)) |>
  pull(cell)
knight_moves <- function(cell) {
  files <- letters[1:8]
  moves <- tribble(
    ~dx , ~dy ,
      2 ,   1 , 2 , -1 , -2 , 1 , -2 , -1 ,
      1 ,   2 , 1 , -2 , -1 , 2 , -1 , -2
  )
  x <- match(str_sub(cell, 1, 1), files)
  y <- as.integer(str_sub(cell, 2, 2))
  moves |>
    transmute(
      x = x + dx,
      y = y + dy
    ) |>
    filter(between(x, 1, 8), between(y, 1, 8)) |>
    transmute(cell = str_c(files[x], y)) |>
    filter(!cell %in% blocked) |>
    pull(cell)
}

shortest_path <- function(start, target) {
  queue <- list(start)
  visited <- start
  while (length(queue)) {
    path <- queue[[1]]
    queue <- queue[-1]
    current <- last(path)
    if (current == target) {
      return(path)
    }
    next_cells <- setdiff(knight_moves(current), visited)
    queue <- c(queue, map(next_cells, \(x) c(path, x)))
    visited <- c(visited, next_cells)
  }
  NULL
}
result <- map(input$Destination, \(x) shortest_path(start, x)) %>%
  map_chr(\(x) if (is.null(x)) NA else str_c(x, collapse = "->"))

all.equal(result, test$Path, check.attributes = FALSE)
# Third path gives different proper.
