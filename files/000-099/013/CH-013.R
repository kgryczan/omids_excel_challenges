library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-013.xlsx", range = "B2:B13")
input2 = read_excel("files/CH-013.xlsx", range = "D3:F6", col_names = FALSE) %>%
  unite("new", 1:3, sep = "|", remove = T, na.rm = T) 

test = read_excel("files/CH-013.xlsx", range = "H2:L6") %>% 
  select(2:5) %>%
  as.matrix(.) %>%
  replace(is.na(.), 0)

colnames(test) = c("pv", "wind", "bat", "ev")

result = input1 %>%
   mutate(pv = str_detect(`Article Titles`, input2$new[[1]]),
                     wind = str_detect(`Article Titles`, input2$new[[2]]),
                     bat = str_detect(`Article Titles`, input2$new[[3]]),
                     ev = str_detect(`Article Titles`, input2$new[[4]])) %>%
   mutate(across(pv:ev, ~ifelse(. == TRUE, 1, 0))) %>%
   mutate(pv_ev = ifelse(pv == 1 & ev == 1, 1, 0),
          wind_bat = ifelse(wind == 1 & bat == 1, 1, 0),
          pv_wind = ifelse(pv == 1 & wind == 1, 1, 0),
          bat_ev = ifelse(bat == 1 & ev == 1, 1, 0),
          pv_bat = ifelse(bat == 1 & pv == 1, 1, 0),
          wind_ev = ifelse(wind == 1 & ev == 1, 1, 0)) %>%
  select(-c(pv, wind, bat, ev)) %>%
  pivot_longer(cols = -`Article Titles`, names_to = "Technology", values_to = "Value") %>%
  mutate(Technology2 = str_replace(Technology, "([a-z]+)_([a-z]+)", "\\2_\\1")) %>%
  unite(Tech, Technology, Technology2, sep = "|", remove = T) %>%
  separate_rows(Tech, sep = "\\|") %>%
  separate(Tech, into = c("Technology", "Technology2"), sep = "_", remove = T) %>%
  select(-`Article Titles`) %>%
  pivot_wider(names_from = Technology2, values_from = Value, 
              values_fn = list(Value = sum), values_fill = list(Value = 0))  %>%
  select(` ` = Technology, pv, wind, bat, ev) %>%
  arrange(factor(` `, levels = c("pv", "wind", "bat", "ev"))) %>%
  select(-` `) %>%
  as.matrix(.)
  

identical(result, test)
# [1] TRUE
