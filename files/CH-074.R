library(tidyverse)
library(readxl)

path = 'files/CH-074 Determining missing fields.xlsx'
input = read_excel(path, range = "B2:C15")
test  = read_excel(path, range = "F2:H6")

result = input %>%
  mutate(cumsum = cumsum(`Info...1` == "Name")) %>%
  select(-Info...2) %>% 
  summarise(n = n(), .by = c(cumsum, `Info...1`)) %>%
  pivot_wider(names_from = `Info...1`, values_from = n, values_fill = list(n = 0)) %>%
  pivot_longer(cols = -cumsum, names_to = "Info", values_to = "n") %>%
  pivot_wider(names_from = n, values_from = Info, values_fn = list) %>%
  select(`Record No` = 1, `Missing fields` = 4, `Duplicated Fields` = 3) %>%
  mutate(`Missing fields` = map_chr(`Missing fields`, ~ifelse(is.null(.x), "-", paste(.x, collapse = ", "))),
         `Duplicated Fields` = map_chr(`Duplicated Fields`, ~ifelse(is.null(.x), "-", paste(.x, collapse = ", "))),
         `Record No` = as.numeric(`Record No`))
         
print(result)
print(test)
# One field differs, because there is empty cell where hyphen should be in H3