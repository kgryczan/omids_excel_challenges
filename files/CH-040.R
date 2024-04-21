library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-040 Cross Selling.xlsx", range = "B2:F26")
input2 = read_excel("files/CH-040 Cross Selling.xlsx", range = "H3:H7", col_names = "Scenario")
test   = read_excel("files/CH-040 Cross Selling.xlsx", range = "K2:L7")

r1 = input1 %>%
  summarise(products = list(unique(Product)), .by = `Invoice ID`)

scen_products = input2 %>%
  mutate(Scenario_split = map(Scenario, ~str_split(.x, ",")[[1]]))

r2 = expand_grid(prod = r1$products, scen = scen_products$Scenario_split) %>%
  left_join(r1, by = c("prod" = "products")) %>%
  select(`Invoice ID`, everything()) %>%
  mutate(is_present = map2_lgl(scen, prod, ~all(.x %in% .y))) %>%
  filter(is_present) %>%
  mutate(diff = map2(scen, prod, ~setdiff(.y, .x))) %>%
  select(scen, diff, `Invoice ID`) %>%
  arrange(scen) %>%
  unnest(cols = c(diff)) %>%
  summarise(invoices = n_distinct(`Invoice ID`), .by = c(scen, diff)) %>%
  arrange(scen, desc(invoices)) %>%
  slice(1, .by = "scen") %>%
  left_join(scen_products, by = c("scen" = "Scenario_split")) %>%
  select(Scenario, diff)


colnames(r2) = colnames(test)

identical(r2, test)
# [1] TRUE

