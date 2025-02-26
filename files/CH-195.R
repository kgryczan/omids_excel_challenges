library(tidyverse)
library(readxl)

path = "files/CH-195 Missing Char.xlsx"
input = read_excel(path, range = "B2:B7")
test  = read_excel(path, range = "D2:D7")

transform_text <- function(text) {
  chars <- substr(text, 1, 2) 
  
  for (i in seq(3, nchar(text))) {
    char <- substr(text, i, i)  
    cond <- ((nchar(chars) + 1) %% 3 == 0) && (char != "/") 
    chars <- paste0(chars, ifelse(cond, "-", ""), char)
  }
  
  return(chars)
}

result = input %>%
  mutate(result = map_chr(ID, transform_text))

all.equal(result$result, test$ID, check.attributes = FALSE) # TRUE
