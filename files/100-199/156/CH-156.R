library(tidyverse)
library(readxl)

path = "files/CH-156 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B8")
test  = read_excel(path, range = "D2:F8")

result = input %>%
  mutate(ID.1 = ifelse(nchar(ID) %% 2 == 0, 
                       substr(ID, 1, nchar(ID)/2), 
                       substr(ID, 1, nchar(ID)/2)),
         ID.2 = ifelse(nchar(ID) %% 2 == 0, 
                       substr(ID, nchar(ID)/2 + 1, nchar(ID)), 
                       substr(ID, nchar(ID)/2 + 1, nchar(ID)/2 + 1)),
         ID.3 = ifelse(nchar(ID) %% 2 == 0, 
                       NA, 
                       substr(ID, nchar(ID)/2 + 2, nchar(ID)))) %>%
    select(-ID)

all.equal(result, test, check.attributes = FALSE)
# only one discrepancy from original solution                                                                                                               