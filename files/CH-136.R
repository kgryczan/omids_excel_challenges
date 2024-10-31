library(tidyverse)
library(readxl)
library(charcuterie)

path = "files/CH-136 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B8")
test  = read_excel(path, range = "D2:F8", col_types = "text")

separate_by_double = function(string) {
  chars = chars(string)
  for (i in 1:(length(chars) - 1)) {
    if (chars[i] == chars[i + 1]) {
      chars[i] = paste0(chars[i], ",")
    }
  }
  df = data.frame(chars = string(chars)) %>% separate(chars, into = c("ID.1","ID.2","ID.3"), sep = ",")
  
  print(df)
}

result = map_dfr(input$ID, separate_by_double)

all.equal(result, test, check.attributes = FALSE)
# 21 in test has dot and decimal zero. 
