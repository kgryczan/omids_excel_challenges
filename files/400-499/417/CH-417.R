library(tidyverse)
library(readxl)

path <- "400-499/417/CH-417 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:D12")
test <- read_excel(path, range = "G3:H9")

result = input %>%
  mutate(srow = paste0(pmin(FROM, TO), "-", pmax(FROM, TO))) %>%
  mutate(group = consecutive_id(srow)) %>%
  mutate(row = first(paste0(FROM, "-", TO)), .by = group) %>%
  summarise(
    `TOTA; QUANTITY` = sum(QUANTITY, na.rm = TRUE),
    .by = c(row, group)
  ) %>%
  select(-group)

all.equal(result, test)
# incorrect results in test
