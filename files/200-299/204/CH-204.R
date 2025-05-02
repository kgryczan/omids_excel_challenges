library(tidyverse)
library(readxl)

path = "files/CH-204 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "H2:J19")

result = input %>%
  mutate(Group = accumulate(Cost, 
                              ~ if (.x$sum + .y > 150 | .x$count == 3) 
                                list(sum = .y, count = 1, group = .x$group + 1) 
                              else 
                                list(sum = .x$sum + .y, count = .x$count + 1, group = .x$group),
                              .init = list(sum = 0, count = 0, group = 1)
  )[-1] %>% map_int("group"))

# Solution has differences in Cost so Groups are not matching.