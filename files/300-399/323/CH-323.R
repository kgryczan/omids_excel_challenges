library(tidyverse)
library(readxl)

path = "300-399/323/CH-323 Pattern Combinations.xlsx"
input = read_excel(path, range = "B2:C12")
test  = read_excel(path, range = "E2:E4")

n = nrow(input)
result <- input %>%
  mutate(group = map2(1:n, 1:n, ~ rep(.x, .y)) %>% unlist() %>% head(n)) %>%
  mutate(f_word = ifelse(group %% 2 == 1, `Column 1`, `Column 2`),
         s_word = ifelse(group %% 2 == 0, `Column 1`, `Column 2`)) %>%
  summarise(f_word = paste(f_word, collapse = ""),
            s_word = paste(s_word, collapse = "")) %>%
  pivot_longer(everything(), values_to = "Combinations") %>%
  select(-name)

all.equal(result, test)