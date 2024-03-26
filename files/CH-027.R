library(tidyverse)
library(readxl)

input = read_excel("files/CH-027 Extract Numbers.xlsx", range = "B1:B13")
test  = read_excel("files/CH-027 Extract Numbers.xlsx", range = "E1:h13", col_names = T)
colnames(test) = c("V1", "V2", "V3", "V4")

result = input %>%
  mutate(strings = str_extract_all(`Question Tables`, "\\((\\d+)\\)")) %>%
  unnest_wider(strings, names_sep = "") %>%
  mutate(across(-`Question Tables`, ~ str_remove_all(., "\\(|\\)") %>% as.numeric())) %>%
  select(-`Question Tables`) 

colnames(result) = c("V1", "V2", "V3", "V4")

identical(result, test)
# [1] TRUE
