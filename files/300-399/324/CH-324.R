library(tidyverse)
library(readxl)

path = "300-399/324/CH-324 Text Cleaning.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:D9")

input$Level = str_remove(str_replace_all(input$Level, "(Under Ground|Upper Ground|Ground)", "\\1,"), ",$")

all.equal(input$Level, test$Level)
