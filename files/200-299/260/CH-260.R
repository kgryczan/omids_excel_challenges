library(tidyverse)
library(readxl)

path = "files/200-299/260/CH-260 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C11")
test  = read_excel(path, range = "E2:G11")

inp = input$Value
names(inp) = input$ID

k           = 3
group_size  = length(inp) / k
target      = sum(inp) / k

valid_groups  = combn(names(inp), k, simplify = FALSE) %>%
  keep(~ sum(inp[.x]) == target)

all_groups = expand.grid(valid_groups, valid_groups, valid_groups) %>%
  rowwise() %>%
  mutate(group = list(c_across(everything()))) %>%
  mutate(group = list(unique(unlist(group)))) %>%
  ungroup() %>%
  filter(lengths(group) == 9) %>%
  unnest_wider(starts_with("Var"), names_sep = "_") %>%
  unite("Var1", starts_with("Var1"), sep = "", na.rm = TRUE) %>%
  unite("Var2", starts_with("Var2"), sep = "", na.rm = TRUE) %>%
  unite("Var3", starts_with("Var3"), sep = "", na.rm = TRUE) %>%
  mutate(unique_group = pmap_chr(list(Var1, Var2, Var3), ~ sort(c(..1, ..2, ..3)) %>% paste(collapse = " "))) %>%
  summarise(sekw = list(group), .by = unique_group) %>% 
  select(-sekw)

print(paste0("Possible sequence by IDs:", all_groups$unique_group))
# "Possible sequence by IDs:148 259 367" 
# "Possible sequence by IDs:156 278 349"