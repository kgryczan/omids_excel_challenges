library(tidyverse)
library(readxl)
library(janitor)

path = "files/300-399/321/CH-321 Correlation.xlsx"
input1 = read_excel(path, range = "B2:F8")
input2 = read_excel(path, range = "B13:E19") %>%
  arrange(Year)
test  = read_excel(path, range = "H2:L5") %>%
  select(y = 1, everything()) %>%
  column_to_rownames(var = 'y')

correlation_matrix = cor(input2 %>% select(-Year), 
                         input1 %>% select(-Year), 
                         use = "pairwise.complete.obs")

all.equal(correlation_matrix, as.matrix(test))
# [1] TRUE  