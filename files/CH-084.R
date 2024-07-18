  library(tidyverse)
  library(readxl)
  
  path = "files/CH-84 Normal Distribution.xlsx"
  input1 = read_excel(path, range = "B2:L13")
  input2 = read_excel(path, range = "N2:N9")
  test   = read_excel(path, range = "O2:O9")
  
  result1 = input1 %>%
    pivot_longer(cols = -c(1), names_to = "Z1", values_to = "prob") %>%
    mutate(Z1 = as.numeric(Z1), 
           Z_tot = Z1 + Z) %>%
    select(Z = Z_tot, prob)
  
  result2 = tibble(Probability = input2$Probability) %>%
    rowwise() %>%
    mutate(Z = result1 %>%
             mutate(diff = abs(prob - Probability)) %>%
             filter(diff == min(diff)) %>%
             pull(Z)) %>%
    ungroup()
    
  all.equal(result2$Z, test$Z)
  #> [1] TRUE