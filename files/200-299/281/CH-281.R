library(tidyverse)
library(readxl)

path = "files/200-299/281/CH-281 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C18")
test  = read_excel(path, range = "G2:H5")

result = input %>%
  mutate(cplus = (cumsum(Result == "+") - 1) %/% 4 + 1,
         Date = format(Date, "%d/%b/%Y")) %>%
  mutate(count = sum(Result == "+"),
         Group = paste0(first(Date), " - ", ifelse(count < 4, "NA", last(Date))), 
         `number of dates` = ifelse(count < 4, "-", as.character(n())),
         .by = cplus) %>%
  select(Group, `number of dates`) %>%
  distinct()

all.equal(result, test)
# > [1] TRUE