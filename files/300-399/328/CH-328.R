library(tidyverse)
library(readxl)

path <- "300-399/328/CH-328 Text Cleaning.xlsx"
input <- read_excel(path, range = "B2:B9")
test  <- read_excel(path, range = "D2:D9")

result = input %>%
  mutate(Level = Level %>%
           str_replace_all("Ground", "Ground,") %>%
           str_replace_all(",$", "") %>%
           str_split(", ") %>%
           map_chr(~ paste(unique(.x), collapse = ", ")))
