library(tidyverse)
library(readxl)

path = "files/CH-146 Column Splitting.xlsx"
input = read_excel(path, range = "B2:B8")
test  = read_excel(path, range = "D2:F8")

result = input %>%
  separate(ID, into = c("ID.1", "ID.2", "ID.3"), sep = "\\|", fill = "right") %>%
  mutate(ID.1 = ifelse(is.na(ID.1), NA, ID.1),
         ID.2 = ifelse(is.na(ID.2), NA, paste(ID.1, ID.2, sep = "")),
         ID.3 = ifelse(is.na(ID.3), NA, paste(ID.2, ID.3, sep = "")))

all.equal(result, test)
#> [1] TRUE