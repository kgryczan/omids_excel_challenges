library(tidyverse)
library(readxl)

path = "files/CH-003.xlsx"
input = read_excel(path, range = "B2:C7")
test  = read_excel(path, range = "H2:I33")

# map on sequence 1:5 combn on input$ID

result = map(1:5, ~combn(input$ID, .x, simplify = FALSE)) %>%
  flatten() %>%
  imap(function(sublist, parent_idx) {
  data.frame(parent_index = parent_idx,ID = sublist) %>%
    pivot_longer(-parent_index)
}) %>%
  bind_rows() %>%
  left_join(input, by = c("value" = "ID")) %>%
  summarise(`ID Combination` = paste(value, collapse = ","), 
            `Total value (cost)` = sum(`value (cost)`),
            .by = parent_index) %>%
  select(-parent_index)

identical(result, test)