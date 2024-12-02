library(tidyverse)
library(readxl)

path = "files/CH-152 Extract from Text.xlsx"
input = read_excel(path, range = "B2:C7")
test  = read_excel(path, range = "E2:H7")

split_on_top_level <- function(s) {
  chars <- strsplit(s, "")[[1]]
  level <- 0
  current <- ""
  result <- c()
  for (char in chars) {
    if (char == '{') level <- level + 1
    if (char == '}') level <- level - 1
    if (char == ',' && level == 0) {
      result <- c(result, current)
      current <- ""
    } else {
      current <- paste0(current, char)
    }
  }
  if (nchar(current) > 0) result <- c(result, current)
  return(result)
}

result = input %>%
  mutate(components = map(Value, split_on_top_level)) %>%
  select(-Value) %>%
  unnest_wider(components, names_sep = "") %>%
  rename_with(~paste0("List.", seq_along(.)), starts_with("components"))

all.equal(result, test)
#> [1] TRUE