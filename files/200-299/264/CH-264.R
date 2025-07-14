library(tidyverse)
library(readxl)

path = "files/200-299/264/CH-264 Extract from Text.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:E7")

extract_substrings <- function(x) {
  n      <- str_length(x)
  starts <- rep(seq_len(n), times = rev(seq_len(n)))
  lengths <- sequence(rev(seq_len(n)))
  
  purrr::map2_chr(starts, lengths, 
                  ~ str_sub(x, .x, .x + .y - 1))
}

result = input %>%
  mutate(substrings = map(Text, extract_substrings)) %>%
  unnest(substrings) %>%
  mutate(substring_length = str_length(substrings)) %>%
  mutate(n = n(), .by = c(Text, substrings)) %>%
  filter(n > 1) %>%
  distinct() %>%
  slice_max(substring_length, n = 1, by = Text) %>%
  select(Text, Pattern = substrings) 

# answer slightly different from the original, but it is correct