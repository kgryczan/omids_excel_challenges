library(tidyverse)
library(readxl)

path <- "300-399/352/CH-352 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:B9") %>% pull()
test <- read_excel(path, range = "F3:H13")

result <- combn(input, 3, simplify = FALSE) %>%
  keep(~ .x[1] == input[1]) %>%
  map_dfr(
    ~ tibble(
      g1 = paste(.x, collapse = ", "),
      g2 = paste(setdiff(input, .x), collapse = ", ")
    )
  ) %>%
  select(`Group 1` = g1, `Group 2` = g2) %>%
  mutate(`Group #` = row_number(), .before = `Group 1`)

all.equal(result, test)
