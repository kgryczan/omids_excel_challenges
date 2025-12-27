library(tidyverse)
library(readxl)

path <- "300-399/347/CH-347 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "F3:I8")

result = input %>%
  mutate(
    ID = str_replace_all(ID, "(?<=\\D{2})(?=\\d{2})|(?<=\\d{2})(?=\\D{2})", "|")
  ) %>%
  separate_wider_delim(
    ID,
    delim = "|",
    names_sep = " ",
    too_few = "align_start"
  )

all.equal(result, test)
# [1] TRUE
