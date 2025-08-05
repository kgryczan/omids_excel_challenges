library(tidyverse)
library(readxl)
library(charcuterie)

path = "files/200-299/275/CH-275 Text Matching.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:E8")

r1 = input %>%
  mutate(ID_clean = str_remove_all(ID, "[^[:alnum:]]"),
         chars_id = map(ID_clean, ~ unique(chars(.x))))

r2 = expand.grid(i = seq_len(nrow(r1)), j = seq_len(nrow(r1))) %>%
  filter(i < j) %>%
  mutate(
    inter = map2(r1$chars_id[i], r1$chars_id[j], ~ intersect(sort(.x), sort(.y)))
  ) %>%
  filter(map_int(inter, length) >= 3) %>%
  transmute(`ID 1` = r1$ID[j], `ID 2` = r1$ID[i])

# the same pairs in different order