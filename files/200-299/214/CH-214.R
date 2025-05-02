library(tidyverse)
library(readxl)

path = "files/CH-214Column Splitting.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:F7")

generate_substrings <- function(str) {
  n <- str_length(str)
  map_dfr(1:n, function(start) {
    map_dfr(start:n, function(end) {
      tibble(substring = str_sub(str, start, end))
    })
  })
}

subs = generate_substrings("1234567890")
subs = subs %>%
  filter(str_length(substring) > 1) 

result = crossing(ID = input$ID, match = subs$substring) %>%
  filter(str_detect(ID, fixed(match))) %>%
  slice_max(str_length(match), by = ID) %>
  mutate(
    before = str_extract(ID, paste0(".*(?=", match, ")")),
    after = str_extract(ID, paste0("(?<=", match, ").*"))
  ) %>%
select(before, match, after)

colnames(result) = colnames(test)

all.equal(result, test)
#> [1] TRUE