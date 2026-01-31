library(tidyverse)
library(readxl)

path <- "300-399/359/CH-359 Replacement.xlsx"
input <- read_excel(path, range = "B3:E10")
test <- read_excel(path, range = "G3:J10")

result = input %>%
  add_count(`Customer ID`) %>%
  mutate(`Customer ID` = ifelse(n == 1, "Other", `Customer ID`)) %>%
  select(-n)

all.equal(result, test)
# [1] TRUE
