library(tidyverse)
library(readxl)

input = read_excel('files/CH-042 Revisit after surgury.xlsx', range = "B2:E27")
test  = read_excel('files/CH-042 Revisit after surgury.xlsx', range = "I2:K4")

result = input %>%
  group_by(`Patient-ID`, Gander) %>%
  arrange(Date) %>%
  summarise(seq = paste0(Referral, collapse = ' -> ')) %>%
  ungroup() %>%
  filter(str_detect(seq, "Surgery -> ")) %>%
  summarise('No of re-visit after surgery' = n() %>% as.numeric(),
            'Patient ID' = paste0(sort(`Patient-ID`), collapse = ', '),
            .by = Gander) %>%
  select(Gender = Gander, everything())

identical(result, test)  

