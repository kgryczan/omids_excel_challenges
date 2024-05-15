library(tidyverse)
library(readxl)

input = read_excel("files/CH-052 Find missing Numbers.xlsx", range = "B2:B15")
test  = read_excel("files/CH-052 Find missing Numbers.xlsx", range = "J2:J7")

full_s = full_seq(c(min(input$Input), max(input$Input)), 1)
missing = setdiff(full_s, input$Input)

identical(missing, test$`Missing Numbers`) 
# [1] TRUE
