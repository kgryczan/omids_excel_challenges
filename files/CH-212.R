library(tidyverse)
library(readxl)

path = "files/CH-212 Remove duplicate.xlsx"
input = read_excel(path, range = "B2:E16")
test  = read_excel(path, range = "G2:G11")

result = list(input$`List 1`, input$`List 2`, input$`List 3`, input$`List 4`) %>%
  unlist() %>%
  enframe(name = NULL) %>%
  count(value) %>%
  filter(n == 1) %>%
  select(`Item Code` = value)

# X-025 and X-022 are repeating