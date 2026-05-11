library(tidyverse)
library(readxl)
library(igraph)

path <- "400-499/410/CH-410 - Non-attacking Bishops Problem.xlsx"
test <- read_excel(path, range = "L3:L9")
used <- c("a2", "a5", "c2")
cols <- letters[1:8]

get_diag <- function(pos) {
    c <- match(str_sub(pos, 1, 1), cols)
    r <- as.integer(str_sub(pos, 2))
    tibble(pos, left_diag = paste0("L", c + r), right_diag = paste0("R", c - r))
}

used_diags <- used |> map(get_diag) |> list_rbind() |> unlist() |> unique()

free <- expand_grid(col = cols, row = 1:8) |>
    transmute(pos = str_c(col, row)) |>
    pull(pos) |>
    map(get_diag) |>
    list_rbind() |>
    filter(
        !pos %in% used,
        !left_diag %in% used_diags,
        !right_diag %in% used_diags
    )

matching <- free |>
    select(from = left_diag, to = right_diag) |>
    graph_from_data_frame(directed = FALSE) |>
    (\(g) {
        V(g)$type <- str_starts(V(g)$name, "L")
        max_bipartite_match(g)$matching
    })()

added <- tibble(from = names(matching), to = unname(matching)) |>
    filter(!is.na(to), str_starts(from, "L")) |>
    left_join(
        free |> select(pos, from = left_diag, to = right_diag),
        by = c("from", "to")
    ) |>
    pull(pos)

result <- sort(unique(added))
