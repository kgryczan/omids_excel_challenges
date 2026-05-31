library(tidyverse)
library(readxl)
library(igraph)

path <- "400-499/420/CH-420 - Knight Distance Problem.xlsx"
input <- read_excel(path, range = "L3:L6")
test <- read_excel(path, range = "M3:M6")
start = "A2"

clean_loc <- function(x) str_to_upper(str_trim(x))
xy_to_loc <- function(x, y) str_c(LETTERS[x], y)

knight_path <- function(start, end, n = 8) {
  start <- clean_loc(start)
  end <- clean_loc(end)

  moves <- tidyr::expand_grid(dx = c(-2, -1, 1, 2), dy = c(-2, -1, 1, 2)) |>
    filter(abs(dx) != abs(dy))
  edges <- tidyr::expand_grid(x = 1:n, y = 1:n) |>
    tidyr::crossing(moves) |>
    mutate(x2 = x + dx, y2 = y + dy) |>
    filter(between(x2, 1, n), between(y2, 1, n)) |>
    transmute(from = xy_to_loc(x, y), to = xy_to_loc(x2, y2))
  g <- igraph::graph_from_data_frame(edges, directed = FALSE)
  if (!all(c(start, end) %in% igraph::V(g)$name)) {
    return(NA_character_)
  }
  igraph::shortest_paths(g, from = start, to = end)$vpath[[1]] |>
    names() |>
    str_c(collapse = "->") %>%
    str_to_lower()
}

result = input %>%
  mutate(Path = map2_chr(start, Destination, knight_path))
# different ways found as well :D
