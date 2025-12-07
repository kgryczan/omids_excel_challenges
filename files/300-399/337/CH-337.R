library(tidyverse)
library(readxl)

path <- "300-399/337/CH-337 Rows Grouping.xlsx"
input <- read_excel(path, range = "B2:C11")
test <- read_excel(path, range = "G2:H7")

result = input %>%
  separate_wider_delim(
    cols = Level,
    delim = " ",
    names = c("Level1", "Level2"),
    too_few = "align_start"
  ) %>%
  summarise(
    Level = paste0(first(Level1), " ", paste(Level2, collapse = ",")) %>%
      str_trim(),
    .by = `Issue ID`
  )

all.equal(result, test)
# [1] TRUE
