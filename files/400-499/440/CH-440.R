library(tidyverse)
library(readxl)
library(igraph)

path <- "400-499/440/CH-440 - Knight Distance Problem.xlsx"
start <- "A2"
end <- "F7"
blocked <- expand_grid(
  file = c("C", "D"),
  rank = 1:6
) %>%
  transmute(cell = paste0(file, rank)) %>%
  pull(cell)
test <- read_excel(path, range = "L3:L6") %>%
  mutate(`example Paths` = str_replace_all(`example Paths`, " ", ""))

blocked <- c(outer(c("C", "D"), 1:6, paste0))
cells <- expand_grid(x = 1:8, y = 1:8) %>%
  mutate(cell = paste0(LETTERS[x], y)) %>%
  filter(!cell %in% blocked)
moves <- expand_grid(
  dx = c(-2, -1, 1, 2),
  dy = c(-2, -1, 1, 2)
) %>%
  filter(abs(dx) + abs(dy) == 3)
edges <- tidyr::crossing(
  cells %>% rename(x1 = x, y1 = y, from = cell),
  moves
) %>%
  transmute(
    from,
    x2 = x1 + dx,
    y2 = y1 + dy
  ) %>%
  inner_join(
    cells %>% rename(x2 = x, y2 = y, to = cell),
    by = c("x2", "y2")
  ) %>%
  select(from, to)
g <- graph_from_data_frame(edges, directed = FALSE)
sp <- all_shortest_paths(
  g,
  from = "A2",
  to = "F7"
)$res
paths <- map(sp, as_ids) %>%
  unique() %>%
  purrr::map_chr(., paste, collapse = "->")

paths # there are 2 identical (by sight).
