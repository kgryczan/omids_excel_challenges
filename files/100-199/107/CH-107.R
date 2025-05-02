library(tidyverse)
library(readxl)

path = "files/CH-107 Matching Tables.xlsx"

T1 = read_excel(path, range = "B2:C9")
T2 = read_excel(path, range = "E2:F9")
test = read_excel(path, range = "H2:I12")

T_full = tibble(`Question ID` = str_c("Q-", 1:10)) %>%
  full_join(T1, by = "Question ID") %>%
  full_join(T2, by = "Question ID") %>%  
  arrange(desc(parse_number(`Question ID`))) %>%
  mutate(Response = case_when(
    is.na(Response.x) & !is.na(Response.y) ~ Response.y,
    !is.na(Response.x) & is.na(Response.y) ~ Response.x,
    !is.na(Response.x) & !is.na(Response.y) ~ Response.y,
    TRUE ~ Response.x
  )) %>%
  select(-Response.x, -Response.y)

identical(T_full, test)
#> [1] TRUE
