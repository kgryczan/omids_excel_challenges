library(tidyverse)
library(readxl)

path <- "400-499/460/CH-460 - Knight Distance Problem.xlsx"
input <- read_excel(path, sheet = "Sheet1", range = "B4:J11", col_names = FALSE)
board <- as.matrix(input[, -1])
cells <- crossing(r = 0:7, c = 0:7) %>%
  mutate(value = as.character(as.vector(t(board)))) %>%
  filter(value != "x")
moves <- tribble(
  ~dr , ~dc , 2 , 1 , 2 , -1 , -2 , 1 , -2 , -1 , 1 , 2 , 1 , -2 , -1 , 2 , -1 , -2
)
start <- c(6, 0) # A2
path <- list(start)
free <- function(q) !any(map_lgl(path, \(p) all(q == p)))
degree <- function(n) {
  sum(map2_lgl(moves$dr, moves$dc, \(dr, dc) {
    free(c(n$r + dr, n$c + dc)) &&
      any(cells$r == n$r + dr & cells$c == n$c + dc)
  }))
}
walk <- function(p) {
  if (length(path) == nrow(cells)) {
    return(TRUE)
  }
  nexts <- moves %>%
    transmute(r = p[1] + dr, c = p[2] + dc) %>%
    semi_join(cells, by = c("r", "c")) %>%
    split(seq(nrow(.)))
  nexts <- nexts[order(map_int(nexts, degree))]
  for (n in nexts) {
    n <- as.numeric(n)
    if (!any(map_lgl(path, ~ identical(n, .x)))) {
      path <<- append(path, list(n))
      if (walk(n)) {
        return(TRUE)
      }
      path <<- path[-length(path)]
    }
  }
  FALSE
}
walk(start)
cell <- function(p) paste0(LETTERS[p[2] + 1], 8 - p[1])
result <- tibble(Step = 0:(length(path) - 1), Cell = map_chr(path, cell))
print(result)
