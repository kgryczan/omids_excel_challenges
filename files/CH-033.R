library(tidyverse)
library(readxl)

input = read_excel("files/CH-033 Noise Removing.xlsx", range = "B1:J16")
test  = read_excel("files/CH-033 Noise Removing.xlsx", range = "L1:L7") 
colnames(test) = "respondent"

r1 = input %>%
  summarize(across(-c(1), ~cor(.x, rowSums(input[,-1]) - .x))) %>%
  pivot_longer(cols = everything(), names_to = "respondent", values_to = "correlation") %>%
  filter(correlation > 0.3) %>%
  select(respondent)

identical(r1, test)
# [1] TRUE
