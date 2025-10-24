library(tidyverse)
library(readxl)

path = "files/300-399/315/CH-315 Consecutive numbers.xlsx"
input = read_excel(path, range = "B1:B14")
test  = read_excel(path, range = "E1:E4")

result = as_tibble(embed(input$Question, 3)[,3:1]) %>%
  filter(V2 - V1 == 1, V3 - V2 == 1) %>%
  unite("Result", V1:V3, sep = ".")

print(result)
