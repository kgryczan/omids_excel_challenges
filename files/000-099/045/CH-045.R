library(tidyverse)
library(readxl)

input = read_excel("files/CH-045 Text Split.xlsx", range = "B2:B17")
test  = read_excel("files/CH-045 Text Split.xlsx", range = "D2:H17")


split = function(text) {
  pattern =  "(\\D+|\\d+)"
  result = str_extract_all(text, pattern, simplify = TRUE) %>% 
    as_tibble() 
  return(result)
}

result = input$ID %>%
  map_dfr(split) %>%
  mutate(across(c(2,4), as.numeric))
  
colnames(result) = colnames(test)

identical(result, test)
# [1] TRUE
