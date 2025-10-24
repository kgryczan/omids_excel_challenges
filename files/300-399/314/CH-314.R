library(tidyverse)
library(readxl)

path = "files/300-399/314/CH-314 Word Pyramid Split.xlsx"
input = read_excel(path, range = "B1:B7")
test  = read_excel(path, range = "C1:C7")

results <- input %>%
  mutate(Result = map(Question, ~ str_c(str_sub(.x, 1, 1:nchar(.x)), collapse = " | ")))

all.equal(results$Result, test$Result, check.attributes = F)
# [1] TRUE