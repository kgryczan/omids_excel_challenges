library(tidyverse)
library(readxl)
library(combinat)

path = "files/CH-90 TSP.xlsx"
input = read_excel(path, range = "B2:G7")
test  = read_excel(path, range = "J2:K26") %>%
  arrange(Cost)

mid_cities = c("B", "C", "D", "E")
city_order_perm = permn(mid_cities) 

city_order = map(city_order_perm, ~c("A", .x, "A")) %>% 
  map_chr(~paste(.x, collapse = "-")) %>%
  tibble(city_order = ., to_sep = .) %>%
  separate_rows(to_sep, sep = "-") %>%
  mutate(lead = lead(to_sep), .by = city_order) %>%
  filter(!is.na(lead))

dist = input %>%
  pivot_longer(names_to = "to", values_to = "dist", -1) %>%
  rename(from = `From To`) 

result = city_order %>%
  left_join(dist, by = c("to_sep" = "from","lead" = "to")) %>%
  mutate(city_order = str_remove_all(city_order, "-")) %>%
  summarise(cost = sum(dist), .by = city_order) %>%
  arrange(cost)

identical(result$cost, test$Cost)
#> [1] TRUE