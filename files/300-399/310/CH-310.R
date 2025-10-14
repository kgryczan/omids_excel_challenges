library(tidyverse)
library(readxl)

input = read_excel("files/300-399/310/CH-310 Numbers Combination.xlsx", range = "B1:B10")
df = expand_grid(i1 = input$Question, i2 = input$Question, i3 = input$Question)
ind = input %>% mutate(ind = row_number())

result = df %>%
  left_join(ind, by = c("i1" = "Question")) %>%
  left_join(ind, by = c("i2" = "Question"), suffix = c("", "2")) %>%
  left_join(ind, by = c("i3" = "Question"), suffix = c("", "3")) %>%
  filter(i2 > i1, i3 > i2, ind < ind2, ind2 < ind3) %>%
  transmute(Result = paste(i1, i2, i3, sep = ",")) %>%
  arrange(Result) %>%
  distinct()

