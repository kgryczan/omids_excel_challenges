library(tidyverse)
library(readxl)
library(jsonlite)

path = "files/200-299/258/CH-258 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B6")
test  = read_excel(path, range = "D2:H6")

result = input %>%
  mutate(across(everything(),
         ~ str_replace_all(.x, "([a-zA-Z0-9\\.]+)", '"\\1"'))) %>%
  mutate(text_parsed = map(Text, ~ fromJSON(.) %>% as_tibble())) %>%
  unnest(text_parsed) %>% 
  select(-Text) 

all.equal(result, test) 
# > [1] TRUE