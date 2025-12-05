library(tidyverse)
library(readxl)

path <- "300-399/336/CH-336 Column Splitting .xlsx"
input <- read_excel(path, range = "B2:B7")
test <- read_excel(path, range = "F2:I7")

result <- input %>%
  mutate(
    ID = str_replace_all(ID, "(?<=\\D)(?=\\d)|(?<=\\d)(?=\\D)", "|")
  ) %>%
  separate_wider_delim(
    ID,
    delim = "|",
    names_sep = " ",
    too_few = "align_start"
  )

all.equal(result, test)
# [1] TRUE
