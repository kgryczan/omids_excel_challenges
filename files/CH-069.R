library(tidyverse)
library(readxl)
library(fuzzyjoin)

path = "files/CH-069 Sales by State.xlsx"

input1 = read_xlsx(path, range = "B2:D41")
input2 = read_xlsx(path, range = "F2:H13")
test   = read_xlsx(path, range = "J2:K7")

input2 = input2 %>%
  arrange(`Customer ID`) %>%
  mutate(end_date = lead(Date, 1), .by = `Customer ID`) %>%
  replace_na(list(end_date = today()))

res = fuzzy_inner_join(input1, input2, 
                       by = c("Customer ID" = "Customer ID", "Date" = "Date", "Date" = "end_date"), 
                       match_fun = list(`==`, `>`, `<=`)) %>%
  summarise(Sales = sum(Quantity), .by = States)

print(res)
