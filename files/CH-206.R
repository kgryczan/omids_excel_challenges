library(tidyverse)
library(readxl)

path = "files/CH-206 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:E7")

result = input %>%
  mutate(rn = row_number()) %>%
  separate_rows(ID, sep = "") %>%
  filter(ID != "") %>%
  mutate(pos = ifelse(row_number() %% 2 == 0, "Even Positions", "Odd Positions"), .by = rn) %>%
  pivot_wider(names_from = pos, values_from = ID, values_fn = ~ paste0(.x, collapse = "")) %>%
  select(-rn)

all.equal(result, test, check.attributes = FALSE)
# There is one mistake in result provided.
