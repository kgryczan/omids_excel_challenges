library(tidyverse)
library(readxl)

path = "files/300-399/316/CH-316 Convert Text.xlsx"
input = read_excel(path, range = "B1:B6")
test  = read_excel(path, range = "C1:C6")

result = input %>%
  mutate(Result = chartr("[a-zA-Z]", "[A-Za-z]", Question))

all.equal(result$Result, test$Result) 
# some result provided are not correct)

# Solution 2 - more expanded
result2 = input %>%
  mutate(Split = strsplit(Question, split = "")) %>%
  unnest(Split) %>%
  mutate(Split = ifelse(Split == str_to_lower(Split), str_to_upper(Split), str_to_lower(Split))) %>%
  summarise(Result = paste0(Split, collapse = ""), .by = Question)

all.equal(result2$Result, test$Result)         
# some result provided are not correct)