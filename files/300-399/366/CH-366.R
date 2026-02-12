library(tidyverse)
library(readxl)

path <- "300-399/366/CH-366 Text Cleaning.xlsx"
input <- read_excel(path, range = "B3:B9")
test <- read_excel(path, range = "E3:E9")

result = input %>%
  mutate(ID = str_replace_all(ID, "(.)\\1+", "\\1"))

all.equal(result$ID, test$ID)
# [1] TRUE
