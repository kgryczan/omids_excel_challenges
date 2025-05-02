library(tidyverse)
library(readxl)

input = read_excel("files/CH-053 OEIS Sequence.xlsx", range = "B2:C12")
test  = read_excel("files/CH-053 OEIS Sequence.xlsx", range = "G2:G67")

range = data.frame(number = 0:100 %>% as.numeric())

are_digits_alphabetical = function(number) {
  digits = as.character(number) %>% strsplit("") %>% unlist()
  replaced = map_chr(digits, ~input$Text[match(.x, input$Number)] %>% as.character())
  all(replaced == sort(replaced))
}

result = range %>% 
  mutate(alphabetical = map_lgl(number, are_digits_alphabetical)) %>%
  filter(alphabetical) %>%
  select(number)

identical(result$number, test$Customer)
#> [1] TRUE 
