library(tidyverse)
library(readxl)

input = read_excel("files/CH-047 Multiple text replaces.xlsx", range = "B2:B11")
dict  = read_excel("files/CH-047 Multiple text replaces.xlsx", range = "E2:F10") %>%
  replace_na(list(Old = " "))
test  = read_excel("files/CH-047 Multiple text replaces.xlsx", range = "J2:J11")

result = input$`Product IDs` %>%
  reduce(dict$Old, ~ str_replace_all(.x, fixed(.y), dict$New[dict$Old == .y]), .init = .) %>%
  tibble(`Product IDs` = .)

identical(result, test)
# [1] TRUE