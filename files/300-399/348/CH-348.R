library(tidyverse)
library(readxl)
library(charcuterie)

path <- "300-399/348/CH-348 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F6")

result = input %>%
  mutate(chars = map(ID, chars)) %>%
  mutate(char_counts = map(chars, ~ table(.))) %>%
  filter(map_lgl(char_counts, ~ any(. >= 3))) %>%
  select(ID)

all.equal(result, test)
# [1] TRUE
