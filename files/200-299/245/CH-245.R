library(tidyverse)
library(readxl)

path = "files/200-299/245/CH-245 Custom Ranking.xlsx"
input = read_excel(path, range = "B2:D17")
test = read_excel(path, range = "F2:I17")

result = input %>%
  mutate(
    group_total = sum(Score),
    group_size = n(),
    in_group_rank = rank(-Score, ties.method = "first"),
    .by = Group
  ) %>%
  mutate(
    group_rank = dense_rank(-group_total),
    Rank = in_group_rank + (group_rank - 1) * group_size
  ) %>%
  select(ID, Group, Score, Rank) %>%
  arrange(Rank)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
