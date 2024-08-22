library(tidyverse)
library(readxl)
library(combinat)

path = "files/CH-101 Subsets.xlsx"
input = read_xlsx(path, range = "B2:C7")
test = read_xlsx(path, range = "H2:I12")

result = combn(input$ID, 3) %>% t() %>% as_tibble() %>%
  unite(ID, V1:V3, sep = ",", remove = FALSE) %>%
  pivot_longer(cols = -ID, names_to = "element", values_to = "value") %>%
  left_join(input, by = c("value" = "ID")) %>%
  summarise(total = sum(`value (cost)`), .by = "ID") 

names(result) = names(test)

identical(result, test)
#> [1] TRUE