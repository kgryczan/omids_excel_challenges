library(tidyverse)
library(readxl)

path = "files/CH-082 Attendance Date.xlsx"
input = read_excel(path, range = "B2:D7")
test  = read_excel(path, range = "F2:G14")

result = input %>%
  mutate(Date = map2(From, To, seq, by = "days")) %>%
  unnest(Date) %>%
  summarise(Supervisors = str_c(Supervisor, collapse = ", "), .by = "Date") 

identical(result, test)
#> [1] TRUE