library(tidyverse)
library(readxl)
library(janitor)

path = "files/CH-181 Table Transformation.xlsx"
input = read_excel(path, range = "C2:C41", col_types = "text")
test  = read_excel(path, range = "E2:H9") %>%
  mutate(From = as.Date(From),
         To = as.Date(To))

result = input %>%
  mutate(row = cumsum(str_detect(Name, "^[A-Z]{3}$"))) %>%
  fill(row, .direction = "down") %>%
  group_by(row) %>%
  mutate(Name1 = first(Name[str_detect(Name, "^[A-Z]{3}$")]),
         prop = ifelse(Name %in% c("From", "To", "Status"), Name, NA)) %>%
  fill(prop, .direction = "down") %>%
  filter(Name != prop | is.na(prop)) %>%
  pivot_wider(names_from = prop, values_from = Name) %>%
  mutate(From = excel_numeric_to_date(as.numeric(From)), 
         To = excel_numeric_to_date(as.numeric(To))) %>%
  ungroup() %>%
  select(Name = Name1, From, To, Status) 

all.equal(result, test)
# [1] TRUE