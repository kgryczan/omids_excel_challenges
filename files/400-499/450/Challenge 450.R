library(tidyverse)
library(readxl)

board <- read_excel(
  "400-499/450/CH-450 - Knight Distance Problem.xlsx",
  sheet = "Sheet1",
  range = "B4:J11",
  col_names = FALSE
)
cells <- expand_grid(row = 8:1, col = letters[1:8]) %>%
  mutate(
    value = as.character(as.vector(t(as.matrix(board[-1])))),
    key = paste(match(col, letters), row, sep = ",")
  )
open <- cells %>% filter(is.na(value) | value != "x") %>% pull(key)
start <- cells %>% filter(value == "♘") %>% pull(key)
targets <- cells %>%
  filter(str_detect(value, "^[0-9]+$")) %>%
  mutate(n = as.integer(value)) %>%
  arrange(n) %>%
  pull(key)
moves <- rbind(
  c(1, 2),
  c(1, -2),
  c(-1, 2),
  c(-1, -2),
  c(2, 1),
  c(2, -1),
  c(-2, 1),
  c(-2, -1)
)

all_paths <- function(square, steps, path) {
  if (!steps) {
    return(if (square == target) list(path) else list())
  }
  p <- as.integer(strsplit(square, ",")[[1]])
  next_squares <- apply(moves, 1, function(m) paste(p + m, collapse = ","))
  next_squares <- next_squares[next_squares %in% open & !next_squares %in% path]
  purrr::flatten(lapply(next_squares, function(x) {
    all_paths(x, steps - 1, c(path, x))
  }))
}

steps <- length(targets)
target <- targets[steps]
routes <- all_paths(start, steps, start)
show <- function(key) {
  p <- as.integer(strsplit(key, ",")[[1]])
  paste0(letters[p[1]], p[2])
}
cat("Paths:", length(routes), "\n")
for (route in routes) {
  cat(paste(vapply(route, show, ""), collapse = " -> "), "\n")
}
cat("Moves:", length(routes[[1]]) - 1, "\n")
