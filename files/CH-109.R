library(tidyverse)
library(readxl)

path = "files/CH-109 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C26")
test  = read_excel(path, range = "G2:H10")
  

result = input %>%
  mutate(group = cumsum(Sales < lag(Sales, default = first(Sales))),
         Date = format(Date, "%m/%d/%Y")) %>%
  summarise(range = paste0(min(Date),"-",max(Date)),
            `Total Sales` = sum(Sales),
            .by = group) 

identical(result$`Total Sales`, test$`Total Sales`)
#> [1] TRUE