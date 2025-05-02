library(tidyverse)
library(readxl)

path = "files/CH-151 Solid Worl.xlsx"
input = read_excel(path, range = "B2:F10")
test  = read_excel(path, range = "H2:J11") %>%
  mutate(across(c("y", "z")), round(., 5))

result = input %>%
  as.matrix() %>% 
  t() %>%
  as.numeric() %>%
  keep(!is.na(.)) %>%
  matrix(ncol = 3, byrow = TRUE) %>%
  as.data.frame() %>%
  setNames(c("x", "y", "z")) %>%
  mutate(across(c("y", "z")), round(., 5))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
