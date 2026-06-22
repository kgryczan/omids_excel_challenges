library(tidyverse)
library(readxl)

path <- "400-499/431/CH-431 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:I10")

result <- input %>%
  mutate(
    chars = str_split(ID, ""),
    seen_before = accumulate(lag(chars, default = list(character())), union),
    new_chars = map2(chars, seen_before, ~ unique(.x[!.x %in% .y]))
  ) %>%
  select(ID = new_chars) %>%
  unnest_wider(ID, names_sep = "")

all.equal(result, test)
# True
