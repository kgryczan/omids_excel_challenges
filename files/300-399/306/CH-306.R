library(tidyverse)
library(readxl)

path = "files/300-399/306/CH-306 Increasing Pair Sum Finder.xlsx"
input = read_excel(path, range = "B1:B10")
test  = read_excel(path, range = "E1:E10")

df = input %>% mutate(id = row_number())

result = expand_grid(a = df$id, b = df$id) %>%
  left_join(df, by = c("a" = "id")) %>%
  left_join(df, by = c("b" = "id"), suffix = c(".a", ".b")) %>%
  filter(a < b, Question.a < Question.b, Question.a + Question.b >= 12) %>%
  transmute(Result = paste(Question.a, Question.b, sep = ","))

all.equal(result, test)
# [1] TRUE