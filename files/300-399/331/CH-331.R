library(tidyverse)
library(readxl)

path <- "300-399/331/CH-331 Pattern Combinations.xlsx"
input <- read_excel(path, range = "B2:C9")
test <- read_excel(path, range = "E2:E4") %>% pull()

result <- input %>%
  mutate(
    p1 = ifelse(row_number() %% 2 == 1, `Column 1`, `Column 2`),
    p2 = ifelse(row_number() %% 2 == 1, `Column 2`, `Column 1`)
  ) %>%
  select(p1, p2) %>%
  summarise(across(everything(), ~ paste(., collapse = ""))) %>%
  pivot_longer(everything(), values_to = "pattern") %>%
  pull(pattern)

all.equal(result, test)
# [1] TRUE
