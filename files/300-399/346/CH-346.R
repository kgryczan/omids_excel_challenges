library(tidyverse)
library(readxl)
library(charcuterie)

path <- "300-399/346/CH-346 Filter.xlsx"
input <- read_excel(path, range = "B3:B10")
test <- read_excel(path, range = "F3:F6")

result = input %>%
  mutate(ID = map(ID, chars)) %>%
  mutate(last_char = map_chr(ID, ~ tail(.x, 1)),
         char_count = map(ID, ~ as.data.frame(table(.x)))) %>%
  unnest(char_count) %>%
  mutate(Freq = ifelse(.x == last_char, 0, Freq)) %>%
  filter(Freq >= 3) %>%
  mutate(ID = map_chr(ID, paste, collapse = "")) %>%
  select(ID)


all.equal(result, test, check.attributes = FALSE)
# [1] TRUE