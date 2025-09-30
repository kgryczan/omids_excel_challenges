library(tidyverse)
library(readxl)
library(janitor)

path = "files/300-399/303/CH-303 Table Transformation.xlsx"
input = read_excel(path, range = "B2:E10")
test  = read_excel(path, range = "G2:J7")

rotate_until_non_na = function(x) {
  if (all(is.na(x))) {
    return(x)                                
  }
  i = min(which(!is.na(x)))
  out = c(x[i:length(x)], x[seq_len(i-1)])
  length(out) = length(x)
  out
}

result <- input %>%
  mutate(across(everything(), rotate_until_non_na)) %>%
  remove_empty("rows") %>%
  row_to_names(1) %>%
  mutate(Date = excel_numeric_to_date(as.numeric(Date)) %>% as.POSIXct(),
         Quantity = as.numeric(Quantity))

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE