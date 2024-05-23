library(tidyverse)
library(readxl)

input1 = read_excel("files/CH-056 Process Efficiency.xlsx", range = "B2:E42") %>% janitor::clean_names()
input2 = read_excel("files/CH-056 Process Efficiency.xlsx", range = "G2:H6") %>% janitor::clean_names()
test   = read_excel("files/CH-056 Process Efficiency.xlsx", range = "J2:K7") %>% janitor::clean_names()

result = input1 %>%
  group_by(production_id) %>%
  summarise(real_sequence = paste0(machinary, collapse = ", "),
            process_type = first(process_type)) %>%
  left_join(input2, by = c("process_type" = "process_type")) %>%
  mutate(aR = str_count(real_sequence, "A"),
         bR = str_count(real_sequence, "B"),
         cR = str_count(real_sequence, "C"),
         dR = str_count(real_sequence, "D"),
         eR = str_count(real_sequence, "E")) %>%
  mutate(aT = str_count(sequence, "A"),
         bT = str_count(sequence, "B"),
         cT = str_count(sequence, "C"),
         dT = str_count(sequence, "D"),
         eT = str_count(sequence, "E")) %>%
  select(aR, bR, cR, dR, eR, aT, bT, cT, dT, eT) %>%
  summarise(across(everything(), sum))

result2 = tibble(
  machinerty = c("A", "B", "C", "D", "E"),
  returne_to_back_again_percent = c((result$aR - result$aT)/result$aT,
  (result$bR - result$bT)/result$bT,
  (result$cR - result$cT)/result$cT,
  (result$dR - result$dT)/result$dT,
  (result$eR - result$eT)/result$eT)
) %>%
  mutate(returne_to_back_again_percent = round(returne_to_back_again_percent, 2))

identical(result2, test)
#> [1] TRUE
