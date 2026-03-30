library(tidyverse)
library(readxl)

path <- "300-399/389/CH-389 Replacement.xlsx"
input <- read_excel(path, range = "B3:E10")
test <- read_excel(path, range = "G3:J10")

result = input %>%
  mutate(Date = as.Date(Date)) %>%
  mutate(Date = Date + pmax(0, 2 - (wday(Date) %% 7)))

# One result different.
