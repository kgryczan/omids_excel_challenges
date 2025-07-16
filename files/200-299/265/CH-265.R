library(tidyverse)
library(readxl)

path = "files/200-299/265/CH-265 Table Transformation.xlsx"
input = read_excel(path, range = "B2:D9")
test  = read_excel(path, range = "F2:I8")

result = input %>%
  mutate(Region = ifelse(str_detect(Column1, "Region"), Column1, NA)) %>%
  fill(Region) %>%
  filter(!duplicated(Column1),
         Column1 != Region) %>%
  setNames(c("Product","Jan","Feb","Region")) %>%
  slice(-1) %>%
  pivot_longer(cols = c("Jan", "Feb"), 
             names_to = "Month", 
             values_to = "Value") %>%
  relocate(Region, .before = Product) %>%
  mutate(Value = as.numeric(Value))

all.equal(result, test, check.attributes = FALSE)  
#> [1] TRUE  
