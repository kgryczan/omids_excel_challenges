library(tidyverse)
library(readxl)
library(charcuterie)

path <- "300-399/345/CH-345 Pattern Recongnition.xlsx"
input <- read_excel(path, range = "B3:B8")
test <- read_excel(path, range = "C3:C8")

result = input %>%
  mutate(Pattern = map(Pattern, chars)) %>%
  mutate(Count = map_int(Pattern, ~ sum(.x[-length(.x)] != .x[-1])))

# difference in 3 example.
