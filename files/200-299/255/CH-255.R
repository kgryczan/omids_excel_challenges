library(tidyverse)
library(readxl)

path = "files/200-299/255/CH-255 Parse HTML.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:G7")

parse_markup = function(text) {
  str_match_all(text, "<([^>]+)>([^<]+)</\\1>")[[1]] %>% 
    as_tibble(.name_repair = "unique") %>% 
    select(tag = 2, value = 3) %>%
    pivot_wider(names_from = tag, values_from = value) 
}

result = input %>%
  mutate(parsed = map(`Raw Text`, parse_markup)) %>%
  unnest(parsed) %>%
  select(-`Raw Text`) %>%
  set_names(names(test)) %>%
  mutate(across(c(ID, Value), as.numeric))

all.equal(result, test, check.attributes = FALSE) 
# TRUE