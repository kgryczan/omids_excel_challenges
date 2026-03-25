library(tidyverse)
library(readxl)

path <- "300-399/387/CH-387 Column Splitting.xlsx"
input <- read_excel(path, range = "B3:B13")
test <- read_excel(path, range = "F3:F13")

result = input %>%
  mutate(ID = str_replace(ID, "(\\d+|\\D+)(\\d+|\\D+)", "\\2\\1"))

all.equal(result$ID, test$ID)
