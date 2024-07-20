library(tidyverse)
library(readxl)

path = "files/CH-085 Custome Ranking.xlsx"
input = read_excel(path, range = "B2:B23") %>%
  mutate(Values = if_else(Values == 51, 56, Values))
test  = read_excel(path, range = "F2:G23")

ab50 = input %>% filter(Values > 50) %>% arrange(Values) %>% pull(Values)
be50 = input %>% filter(Values < 50) %>% arrange(desc(Values)) %>% pull(Values)


if (length(ab50) > length(be50)) {
  be50 = c(be50, rep(NA, length(ab50) - length(be50)))
} else {
  ab50 = c(ab50, rep(NA, length(be50) - length(ab50)))
}

df = data.frame(ab = ab50, be = be50) %>%
  mutate(nr = row_number()) %>%
  pivot_longer(cols = c(ab, be), names_to = "type", values_to = "Values") %>%
  na.omit() %>%
  mutate(t2 = Values - 50 > 0) %>%
  arrange(nr, desc(t2)) %>%
  mutate(Rank = row_number()) %>%
  select(Values, Rank) %>%
  arrange(Values)

