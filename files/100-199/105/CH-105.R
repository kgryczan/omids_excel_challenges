library(tidyverse)
library(readxl)

path = "files/CH-105 Character Repetition.xlsx"
input = read_excel(path, range = "B2:B12")
test = read_excel(path, range = "D2:E8")

result = input %>%
  mutate(Password = Password %>%
           str_to_lower()) %>%
  separate_rows(Password, sep = "") %>%
  select(Character = Password) %>%
  summarise(Repitation = n() %>% as.numeric(), .by = Character) %>%
  filter(Character != "") %>%
  arrange(desc(Repitation), Character) %>%
  head()

identical(result, test)
#> [1] TRUE
