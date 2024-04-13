library(tidyverse)
library(readxl)

input = read_excel("files/CH-036 Pareto Line.xlsx", range = "B2:E14")
test  = read_excel("files/CH-036 Pareto Line.xlsx", range = "H1:H7") %>% na.omit()

result = input %>%
  mutate(row_id = row_number()) %>%
  pmap(., function(...){
    current = tibble(...)
    dominated = any(pmap_lgl(input, function(...){
      other = tibble(...)
      all(other[2:4] > current[2:4])
    }))
    !dominated
  }) %>%
  unlist() %>%
  which() %>%
  tibble(Result = .) %>%
  mutate(Result = as.numeric(Result))

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
