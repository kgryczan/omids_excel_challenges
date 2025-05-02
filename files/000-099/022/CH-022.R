library(tidyverse)
library(readxl)
library(english)

input = read_excel("files/CH-022 Convert Number To Text.xlsx" , range = "B2:B10")
test  = read_excel("files/CH-022 Convert Number To Text.xlsx" , range = "G2:H10")

result = input %>%
  mutate(
    number = as.character(Number),
    integer_part = map(number, ~ strsplit(.x, "\\.")[[1]][1]) %>% as.integer(),
    decimal_part = map(number, ~ strsplit(.x, "\\.")[[1]][2]) %>% as.integer()
  ) %>%
  mutate(
    integer_part_text = map_chr(integer_part, ~ as.character(as.english(.x))),
    decimal_part_text = map_chr(decimal_part, ~ as.character(as.english(.x))),
    Text = ifelse(is.na(decimal_part), 
                  integer_part_text, 
                  paste0(integer_part_text, " point ", decimal_part_text)) %>%
      str_to_sentence() %>%
      str_remove_all(" and")
  ) %>%
  select(Number, Text)
    
identical(result, test)
# [1] TRUE
