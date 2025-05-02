library(tidyverse)
library(readxl)

path = "files/CH-093 Random Selection.xlsx"
input = read_excel(path, range = "B2:C20")
test  = read_excel(path, range = "E2:F7")

result = input %>%
  slice_sample(n = 1, by = Department)

# A tibble: 5 × 2
# Department `Staff ID`
# <chr>      <chr>     
# 1 HR         S_01      
# 2 Marketing  S_03      
# 3 IT         S_10      
# 4 Production S_16      
# 5 R&D        S_15   