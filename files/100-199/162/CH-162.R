library(tidyverse)
library(readxl)

path = "files/CH-162 Extract from Text.xlsx"
input = read_excel(path, range = "B2:C7")
test  = read_excel(path, range = "E2:I7")

r1 = input %>%
  mutate(Value = str_replace_all(Value, "(\\d),\\{", "\\1},\\{")) %>%
  mutate(Value = str_replace_all(Value, "\\{+", "{")) %>%
  mutate(Value = str_replace_all(Value, "\\}+", "}")) %>%
  separate_rows(Value, sep = "(?<=\\}),(?=\\{)") %>%
  mutate(rn = row_number(), .by = ID) %>%
  pivot_wider(names_from = rn, values_from = Value) %>%
  setNames(colnames(test))

all.equal(r1, test, check.attributes = FALSE)
# TRUE