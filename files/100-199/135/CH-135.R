library(tidyverse)
library(readxl)

path = "files/CH-135 Identify the Pattern.xlsx"
input = read_excel(path, range = "B2:D32")
test  = read_excel(path, range = "F2:G5")

count_occurences = function(string, pattern = "+-+") {
  pattern_length = nchar(pattern)
  chars = unlist(strsplit(string, ""))
  matches = integer(0)
  for (i in seq_len(length(chars) - pattern_length + 1)) {
    segment = paste0(chars[i:(i + pattern_length - 1)], collapse = "")
    if (segment == pattern) {
      matches = c(matches, i)
    }
  }
  return(length(matches))
}

result = input %>%
  summarise(Result = str_c(Result, collapse = ""), .by = Product) %>%
  mutate(`Number of repitation` = map_int(Result, count_occurences)) %>%
  select(Product, `Number of repitation`) %>%

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE