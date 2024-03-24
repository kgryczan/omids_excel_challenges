library(tidyverse)
library(readxl)

input = read_excel("files/CH-026 Calculate the spending time.xlsx", range = "B2:E18")
test  = read_excel("files/CH-026 Calculate the spending time.xlsx", range = "G2:L7") %>%
  mutate(across(where(is.numeric), ~round(., 2))) 

r1 <- input %>%
  separate(Duration, into = c("date", "time"), sep = " ") %>%
  separate(time, into = c("hours", "minutes", "seconds"), sep = ":") %>%
  mutate(Duration = as.numeric(hours) * 3600 + as.numeric(minutes) * 60) %>%
  select(1:3,8)

r2 = r1 %>%
  unite(`Person 1`, `Person 2`, col = "pair", sep = "_") %>%
  mutate(pair = map_chr(pair, ~paste(sort(unlist(strsplit(., "_"))), collapse = "_"))) %>%
  separate(pair, into = c("P1", "P2"), sep = "_") %>%
  group_by(P1) %>%
  arrange(P1) %>%
  select(-Date)

r3 = expand.grid(P1 = LETTERS[1:5], P2 = LETTERS[1:5]) %>%
  left_join(r2, by = c("P1", "P2")) %>%
  replace_na(list(Duration = 0)) %>%
  pivot_wider(names_from = P2, values_from = Duration, values_fn = sum) %>%
  column_to_rownames(var = "P1") 

r4 = expand.grid(P1 = LETTERS[1:5], P2 = LETTERS[1:5]) %>%
  left_join(r2, by = c("P1", "P2")) %>%
  replace_na(list(Duration = 0)) %>% 
  pivot_wider(names_from = P1, values_from = Duration, values_fn = sum) %>%
  column_to_rownames(var = "P2")

r5 = r3 + r4

r6 = r5 %>%
  mutate(across(everything(), ~./rowSums(r5))) %>%
  mutate(across(everything(), ~round(., 2))) %>%
  rownames_to_column(var = "Month")%>% mutate(across(- Month, as.numeric)) %>%
  as_tibble()

identical(r6, test)
# [1] TRUE

