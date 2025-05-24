library(tidyverse)
library(readxl)

path = "files/200-299/236/CH-236 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test = read_excel(path, range = "D2:F7")
test[is.na(test)] <- ""

split_id <- function(s) {
  if (str_detect(s, "^[A-Za-z]{3}")) {
    list(
      str_sub(s, 1, 3),
      str_sub(s, 4, 6),
      str_sub(s, 7, str_length(s))
    )
  } else {
    list(s, "", "")
  }
}

result = input %>%
  mutate(`ID.` = map(ID, split_id)) %>%
  unnest_wider(`ID.`, names_sep = "") %>%
  select(-c(1))

all.equal(result, test)
# [1] TRUE
