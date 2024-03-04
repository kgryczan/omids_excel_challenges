library(tidyverse)
library(readxl)

input = read_excel("files/CH-016 .xlsx", range = "B2:C15")
test  = read_excel("files/CH-016 .xlsx", range = "F2:I6")
                                                                                                                                                                      
result = input %>% 
  mutate(name = ifelse(Info...1 == "Name", 1, 0)) %>%
  mutate(name = cumsum(name)) %>%
  pivot_wider(names_from = Info...1, values_from = Info...2, 
              values_fn =  ~ paste(.x, collapse = " and ")) %>%
  select(-name)

identical(result, test)
#> [1] TRUE

