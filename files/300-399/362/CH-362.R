library(tidyverse)
library(readxl)

path <- "300-399/362/CH-362 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:E10")
test <- read_excel(path, range = "H3:I6")

result = input %>%
  mutate(n = n(), .by = `Customer ID`) %>%
  mutate(IDs = ifelse(n == 1, "Other", `Customer ID`)) %>%
  summarise(Sales = sum(`Total Sales`), .by = IDs)

all.equal(result, test)
# [1] TRUE
