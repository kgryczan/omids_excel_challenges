library(tidyverse)
library(readxl)
library(igraph)

path <- "files/CH-180 Hierarchical Structure.xlsx"
input <- read_excel(path, range = "B2:C13")
test <- read_excel(path, range = "E2:F14") %>% arrange(Code)

in2 <- input %>% mutate(code = row_number(), .by = Parent)
g <- graph_from_data_frame(in2, directed = TRUE)
all_paths <- all_simple_paths(g, from = "A", to = V(g))

df <- map_df(all_paths, ~ data.frame(paths = paste(names(.x), collapse = "-")))

result <- df %>%
  mutate(IDs = str_extract(paths, "\\w$"), rn = row_number()) %>%
  mutate(path = str_replace_all(paths, "\\d", ~ in2$code[as.numeric(.x)])) %>%
  separate_rows(paths, sep = "-") %>%
  left_join(in2 %>% add_row(Parent = NA, Child = "A", code = 1), by = c("paths" = "Child")) %>%
  summarise(Code = paste0(code, collapse = "-"), .by = IDs) %>%
  select(Code, IDs) %>%
  add_row(Code = "1", IDs = "A") %>%
  arrange(Code)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE