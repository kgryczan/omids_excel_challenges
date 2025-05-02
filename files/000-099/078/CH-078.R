library(tidyverse)
library(readxl)

path = "files/CH-078 Extract from Text 2.xlsx"

input = read_xlsx(path, range = "B3", col_names = F) %>%
  pull()
test = read_xlsx(path, range = "B6:B11") %>%
  mutate(`Email Address` = str_sub(`Email Address`, 4))

patterns = c(
  "\\d{4}-\\d{2}-\\d{2}",
  "\\d{2}\\/\\d{2}\\/\\d{4}",
  "\\b\\w+ \\d{1,2}[a-z]*?(?: to \\w+ \\d{1,2}[a-z]*)?, \\d{4}\\b"
)

result = input %>%
  str_extract_all(str_c(patterns, collapse = "|")) %>%
  map(~ .x[.x != ""]) 

result = tibble(`Email Address` = result[[1]])


identical(result, test)
# [1] TRUE