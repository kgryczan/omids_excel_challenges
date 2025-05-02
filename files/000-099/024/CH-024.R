library(tidyverse)
library(openxlsx2)

setwd("~/omids_excel_challenges/files/")
file <- "CH-024 Hilight merged dcells.xlsx"
wb = wb_load(file)

df = wb$to_df(fill_merged_cells = F,  dims = "B2:I14", col_names = T) 

process_rows <- function(df, i) {
  df[i,] %>%
    t() %>% 
    as.data.frame() %>% 
    rownames_to_column("row") %>%
    select(-row) %>%
    mutate(row = i, col = row_number()) %>%
    rename(text = 1) %>%
    mutate(gr = cumsum(!is.na(text))) %>%
    filter(n() > 1, .by = gr) %>%
    unite("pos", row, col, sep = "_") %>%
    select(pos) %>%
    unlist()
}

process_cols <- function(df, i) {
  df[,i] %>% 
    as.data.frame() %>% 
    mutate(col = i, row = row_number()) %>%
    rename(text = 1) %>%
    mutate(gr = cumsum(!is.na(text))) %>%
    filter(n() > 1, .by = gr) %>%
    unite("pos", row, col, sep = "_") %>%
    select(pos) %>%
    unlist()
}

rows_merged <- map(1:3, ~process_rows(df, .x)) %>% reduce(c) %>% unique()
cols_merged <- map(1:ncol(df), ~process_cols(df, .x)) %>% reduce(c) %>% unique()

merged_cells_positions <- union(rows_merged, cols_merged) %>%
  unique()

positions = merged_cells_positions %>% 
  as.tibble() %>%
  separate(value, c("row", "col"), sep = "_") %>%
  mutate(row = as.numeric(row), col = as.numeric(col)) %>%
  mutate(val = "X")

all_grid = expand.grid(row = 1:12, col = 1:8) %>%
  left_join(positions, by = c("row", "col")) %>%
  mutate(val = ifelse(is.na(val), "", val)) %>%
  pivot_wider(names_from = col, values_from = val) %>%
  select(-row) 

view(all_grid)
