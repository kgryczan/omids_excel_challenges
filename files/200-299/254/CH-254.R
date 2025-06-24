library(tidyverse)
library(readxl)

path = "files/200-299/254/CH-254 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:I7")

result = input %>%
  mutate(
    hyphen_count = str_count(ID, "-"),
    middle_hyphen = ceiling((hyphen_count + 1) / 2),
    hyphen_loc = str_locate_all(ID, "-")) %>%
  rowwise() %>%
  mutate(middle_hyphen_loc = hyphen_loc[middle_hyphen, 1]) %>%
  ungroup() %>%
  mutate(
    first_part = str_sub(ID, 1, middle_hyphen_loc - 1),
    second_part = str_sub(ID, middle_hyphen_loc + 1, nchar(ID))) %>%
  separate_wider_delim(first_part, delim = "-", too_few = "align_start", names = c("ID.1","ID.2", "ID.3")) %>%
  separate_wider_delim(second_part, delim = "-", too_few = "align_end", names = c("ID.4","ID.5", "ID.6")) %>% 
  select(starts_with("ID."))

all.equal(result, test) 
# > [1] TRUE