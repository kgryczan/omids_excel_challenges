library(tidyverse)
library(readxl)

path = "files/200-299/286/CH-286 Advanced Filtering.xlsx"
input = read_excel(path, range = "B2:E9")
test  = read_excel(path, range = "G2:G4") %>% pull()

result = input %>%
  pivot_longer(-ID) %>%
  mutate(n = n(), .by = value) %>%
  summarise(sum = sum(n), .by = ID) %>%
  filter(sum == 3) %>%
  select(ID) %>%
  pull()

# should be 2 and 4, but provided answer is 2 and 5.