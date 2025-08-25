library(tidyverse)
library(readxl)

path = "files/200-299/285/CH-285 Text Matching.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:E11") %>% arrange(`ID 1`, `ID 2`)

result = input %>%
mutate(rn = row_number(), IDc = str_remove_all(ID, "-")) %>%
  expand_grid(., ., .name_repair = "unique") %>%
  filter(rn...2 > rn...5) %>%
  transmute(ID_left = ID...1, ID_right = ID...4,
            a = IDc...3, b = IDc...6) %>%
  mutate(m1 = map2_int(a, b, ~ sum(str_detect(.x, str_split(.y, "")[[1]]))),
         m2 = map2_int(b, a, ~ sum(str_detect(.x, str_split(.y, "")[[1]])))) %>%
  filter(pmax(m1, m2) >= 3) %>%
  transmute(ID1 = ID_right, ID2 = ID_left) %>%
  arrange(ID1, ID2)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE