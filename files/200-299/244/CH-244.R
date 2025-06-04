library(tidyverse)
library(readxl)

path = "files/200-299/244/CH-244 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:E7")

split_by_sec_del = function(text) {
  hyph_loc = str_locate_all(text, "-")[[1]]
  sl_loc = str_locate_all(text, "\\/")[[1]]

  if (nrow(hyph_loc) < 2 & nrow(sl_loc) < 2) {
    return(text)
  } else if (nrow(hyph_loc) >= 2 & nrow(sl_loc) >= 2) {
    split_loc <- min(hyph_loc[2, 1], sl_loc[2, 1])
  } else if (nrow(hyph_loc) >= 2) {
    split_loc <- hyph_loc[2, 1]
  } else {
    split_loc <- sl_loc[2, 1]
  }
  first_part = str_sub(text, 1, split_loc - 1)
  second_part = str_sub(text, split_loc + 1)
  return(c(first_part, second_part))
}

result = input %>%
  mutate(ID = map(ID, split_by_sec_del)) %>%
  unnest_wider(ID, names_sep = ".")

all.equal(result, test, check.attributes = FALSE)
# TRUE
