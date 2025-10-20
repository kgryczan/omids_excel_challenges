library(tidyverse)
library(readxl)

path = "files/300-399/313/CH-313 Table Transformation.xlsx"
input = read_excel(path, range = "B2:J8")
test  = read_excel(path, range = "L2:O7") %>% mutate(across(everything(), as.character))

shift4 = function(df){
  valid = !is.na(df) & str_trim(as.character(df)) != ""
  start = max.col(valid, ties.method = "first")
  start[!rowSums(valid)] = 1
  map_dfr(seq_len(nrow(df)), function(i) {
    v = unlist(df[i, ], use.names = FALSE)
    vals = v[start[i] + 0:3]; length(vals) = 4
    tibble(Date = vals[1], Product = vals[2], Customer = vals[3], Quantity = vals[4])
  })
}

output = shift4(input) %>%
  filter(row_number() > 1) %>%
  mutate(Date = janitor::excel_numeric_to_date(as.numeric(Date)) %>% as.character())

all.equal(output, test, check.attributes = FALSE)
# [1] TRUE