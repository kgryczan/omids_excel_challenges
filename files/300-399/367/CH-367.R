library(tidyverse)
library(readxl)

path <- "300-399/367/CH-367 Text Cleaning.xlsx"
input <- read_excel(path, range = "B3:B9")
test <- read_excel(path, range = "E3:E9")

result <- input %>%
  mutate(ID = str_replace(ID, "(.+)\\1+", "\\1"))

all.equal(result$ID, test$ID)
# [1] TRUE
