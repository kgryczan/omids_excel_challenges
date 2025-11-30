library(tidyverse)
library(readxl)

path <- "300-399/334/CH-334 Custom Condition.xlsx"
input <- read_excel(path, range = "B2:D11")
test <- read_excel(path, range = "H2:H5")

result = input %>%
  arrange(Date) %>%
  slice_tail(n = 1, by = `Issue ID`) %>%
  filter(Status != "Close") %>%
  pull(`Issue ID`)

# Solution provided not correct
