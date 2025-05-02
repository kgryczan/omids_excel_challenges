library(tidyverse)
library(readxl)

path = "files/CH-201Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:F7")

is_palindrome = function(x) {{stringi::stri_reverse(x) == x}}

result = input %>%
  mutate(is_palindrome = map_lgl(ID, is_palindrome)) %>%
  mutate(vowelloc = str_locate(ID, "[AEIOU]")[,1]) %>%
  mutate(is_even = nchar(ID) %% 2 == 0) %>%
  mutate(`Part 1` = case_when(
    is_palindrome & is_even ~ str_sub(ID, 1, nchar(ID)/2),
    is_palindrome & !is_even ~ str_sub(ID, 1, nchar(ID)/2),
    !is_palindrome ~ str_sub(ID, 1, vowelloc-1)
  ),
  Middle = case_when(
    is_palindrome & is_even ~ NA,
    is_palindrome & !is_even ~ str_sub(ID, nchar(ID)/2+1, nchar(ID)/2+1),
    !is_palindrome ~ str_sub(ID, vowelloc, vowelloc)
  ),
  `Part 2`  = case_when(
    is_palindrome & is_even ~ str_sub(ID, nchar(ID)/2+1, nchar(ID)),
    is_palindrome & !is_even ~ str_sub(ID, nchar(ID)/2+2, nchar(ID)),
    !is_palindrome ~ str_sub(ID, vowelloc+1, nchar(ID))
  )) %>%
  select(`Part 1`, Middle, `Part 2`)

all.equal(test, result, check.attributes = FALSE)
#> [1] TRUE