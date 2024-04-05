library(tidyverse)
library(readxl)

input = read_excel("files/CH-032 Transformation.xlsx", range = "B2:H15", col_names = FALSE)
test  = read_excel("files/CH-032 Transformation.xlsx", range = "J2:L38")

input_header = input %>% 
  filter(!...1 %in% c(1:12)) %>%
  t() %>%
  as.data.frame() %>%
  fill(1, .direction = "down") %>%
  unite("header", V1, V2, sep = "_", na.rm = T) %>%
  pull()

colnames(input) = input_header

input_table = input %>%
  filter(Month %in% c(1:12)) %>%
  pivot_longer(cols = c(2,4,6), names_to = "Year", values_to = "Sales") %>%
  select(-c(2,3,4)) %>%
  separate(col = "Year", into = c("Year", "M")) %>%
  mutate(across(everything(), as.numeric)) %>%
  select(-M) %>%
  arrange(Year, Month)
  
identical(test, input_table)
# [1] TRUE
