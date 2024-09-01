library(tidyverse)
library(readxl)

path = "files/CH-106 Custom Rank.xlsx"
input = read_excel(path, range = "C2:G12")
test  = read_excel(path, range = "L2:M12")

# approach 1
result = input[order(-input$Gold, -input$Silver, -input$Bronze),] 
identical(result$Country, test$Country) 
# [1] TRUE

# approach 2

result = input %>% arrange(-Gold, -Silver, -Bronze)
identical(result$Country, test$Country)
# [1] TRUE