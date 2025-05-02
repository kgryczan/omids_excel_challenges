library(tidyverse)
library(readxl)

path = "files/CH-163 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:D39")
test  = read_excel(path, range = "G2:I17")

result = input %>% 
  unite("ym", Year, Month ,  sep = " ", remove = F) %>%
  mutate(ym = ym(ym),
         Season = quarter(ym)) %>%
  summarise(`Total Sale` = sum(Sale), .by = c(Year, Season))

all.equal(result, test)
# TRUE