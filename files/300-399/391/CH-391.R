library(tidyverse)
library(readxl)

path <- "300-399/391/CH-391 Index.xlsx"
input <- read_excel(path, range = "B3:F23")
test <- read_excel(path, range = "G3:G23")

result = input %>%
  mutate(Mark = ifelse(row_number() == 1, "*", NA_character_), .by = "Customer")

all.equal(result$Mark, test$Mark)
# [1] TRUE
