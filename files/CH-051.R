library(tidyverse)
library(readxl)

input = read_excel("files/CH-051 Purchasing together.xlsx", range = "B2:F26")
test= read_excel("files/CH-051 Purchasing together.xlsx", range = "J2:K7")

result = input %>%
  select(`Invoice ID`, Product, Quantity) %>%
  pivot_wider(names_from = Product, values_from = Quantity, values_fill = list(Quantity = 0)) %>%
  mutate(`A,B` = ifelse(A>0 & B>0, T, F),
         `A,C` = ifelse(A>0 & C>0, T, F),
         `C,D` = ifelse(C>0 & D>0, T, F),
         `A,B,C` = ifelse(A>0 & B>0 & C>0, T, F),
         `A,B,C,D` = ifelse(A>0 & B>0 & C>0 & D>0, T, F)) %>%
  select(`Invoice ID`, `A,B`, `A,C`, `C,D`, `A,B,C`, `A,B,C,D`) %>%
  pivot_longer(cols = -`Invoice ID`, names_to = "Products", values_to = "Purchased") %>%
  filter(Purchased == T) %>% 
  summarise(Count = n() %>% as.numeric(), .by = Products)

identical(result, test)  
# [1] TRUE
