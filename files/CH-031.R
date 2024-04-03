library(tidyverse)
library(readxl)

input = read_excel("files/CH-031 Creat From-To matrix.xlsx", range = "B2:D12")
test  = read_excel("files/CH-031 Creat From-To matrix.xlsx", range = "F2:K7") %>% 
  column_to_rownames(var = "...1") %>%
  as.matrix()

t1 = input %>%
  pivot_wider(names_from = "TO", values_from = "Distance") %>%
  select(From, A, B, C, D, E) %>% 
  column_to_rownames(var = "From") %>%
  as.matrix() %>%
  replace(is.na(.), 0)
  
t2 = t1 %>%
  t()  %>%
  replace(is.na(.), 0)

t = t1 + t2

identical(t, test)
# [1] TRUE


