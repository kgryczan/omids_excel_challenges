library(tidyverse)
library(readxl) 
library(janitor)

path = "files/CH-155 Table Transformation.xlsx"
input = read_excel(path, range = "C2:E23")
test  = read_excel(path, range = "G2:I11")

result = input %>%
  mutate(Description = lead(Description), 
         Qty = lead(Qty,2) %>% as.character()) %>%
  remove_empty("rows") %>%
  replace_na(list(Qty = "-")) %>%
  fill(Date, .direction = "down")

all.equal(result[2:3], test[2:3], check.attributes = FALSE)  
# [1] TRUE

# structure correct, have some problems with date