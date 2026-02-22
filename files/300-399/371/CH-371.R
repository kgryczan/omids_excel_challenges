library(tidyverse)
library(readxl)

path <- "300-399/371/CH-371 Text Cleaning.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "E3:E8")


result = input %>%
  mutate(cleaned = str_remove_all(ID, "(.).*?\\1")) %>%
  select(ID = cleaned)

all.equal(result$ID, test$ID)
# [1] TRUE
