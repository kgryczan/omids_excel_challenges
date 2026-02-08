library(tidyverse)
library(readxl)

path <- "300-399/364/CH-364 Custom Grouping.xlsx"
input <- read_excel(path, range = "B3:C8")
test <- read_excel(path, range = "F3:G7")

input_combinations <- map(
  2:nrow(input),
  ~ combn(input$Price, .x, simplify = FALSE)
) %>%
  unlist(recursive = FALSE) %>%
  keep(~ sum(.x) %in% c(10, 13)) %>%
  map(~ paste(LETTERS[.x], collapse = ",")) %>%
  unlist() %>%
  sort()

# one combination is wrong in test table. should be ACDE, not ABDE (ABDE sum is 12)
