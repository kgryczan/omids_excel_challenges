library(tidyverse)
library(readxl)

path <- "300-399/342/CH-342 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "F3:G8")

result = input %>%
  mutate(ID = str_replace_all(ID, "([A-Z]{2})([0-9]{2})", "\\1-\\2")) %>%
  separate_wider_delim(
    ID,
    delim = "-",
    names_sep = " ",
    too_few = "align_start"
  )

all.equal(result, test)
