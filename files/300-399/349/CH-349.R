library(tidyverse)
library(readxl)

path <- "300-399/349/CH-349 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "F3:K8")

result = input %>%
  mutate(
    ID = str_replace_all(
      ID,
      "(?<=[A-Za-z])(?=[^A-Za-z])|(?<=[0-9])(?=[^0-9])|(?<=[^A-Za-z0-9])(?=[A-Za-z0-9])",
      "|"
    )
  ) %>%
  separate_wider_delim(
    ID,
    delim = "|",
    names_sep = " ",
    too_few = "align_start"
  )

all.equal(result, test)
# Difference in first row
