library(tidyverse)
library(readxl)

path = "files/CH-130 FIFO.xlsx"
input = read_excel(path, range = "B2:D13")
test  = read_excel(path, range = "F2:I11")

i_data = input %>%
  filter(str_starts(Tyoe, "I")) %>%
  uncount(Quantity, .remove = F) %>%
  mutate(In = 1, rn = row_number())

o_data = input %>%
  filter(str_starts(Tyoe, "O")) %>%
  uncount(Quantity, .remove = F) %>%
  mutate(Out = 1, rn = row_number())

all = full_join(i_data, o_data, by = "rn") %>%
  summarise(all = sum(In, na.rm = T), .by = c(Date.x, Date.y, Tyoe.x, Tyoe.y)) %>%
  na.omit() %>%
  mutate(Output = str_sub(Tyoe.y, -1, -1)) %>%
  select(Output, `Registered Date` = Date.y, `Source Date` = Date.x, Quantity = all)

all.equal(all, test, check.attributes = F)
#> [1] TRUE  