library(tidyverse)
library(readxl)

path <- "300-399/338/CH-338 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "F3:K8")

add_splitter_on_char_change <- function(x) {
  stringr::str_replace_all(
    x,
    "(?<=[A-Za-z])(?=[^A-Za-z])|(?<=[^A-Za-z])(?=[A-Za-z])|
     (?<=[0-9])(?=[^0-9])|(?<=[^0-9])(?=[0-9])|
     (?<=[[:punct:]])(?=[^[:punct:]])|(?<=[^[:punct:]])(?=[[:punct:]])",
    "|"
  )
}

result = input %>%
  mutate(ID = map(ID, ~ add_splitter_on_char_change(.))) %>%
  separate_wider_delim(
    ID,
    delim = "|",
    names_sep = " ",
    too_few = "align_start"
  )

all.equal(result, test)
