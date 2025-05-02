library(tidyverse)
library(readxl)
library(hms)

path = "files/CH-142 Table Transformation.xlsx"
input = read_excel(path, range = "B2:E18") 
test  = read_excel(path, range = "G2:J12") %>% 
  mutate(across(c(In, Out), as_hms))

input = input %>% mutate(Time = as_hms(Time))
ins = input %>% filter(Type == "In") %>% rename(In = Time)
outs = input %>% filter(Type == "Out") %>% rename(Out = Time)

result_df = ins %>%
  left_join(outs, by = c("Date", "ID")) %>%
  filter(In < Out) %>%
  group_by(Date, ID, In) %>%
  slice_min(Out) %>%
  ungroup()

unmatched_ins = anti_join(ins, result_df, by = c("Date", "ID", "In"))
unmatched_outs = anti_join(outs, result_df, by = c("Date", "ID", "Out"))

result = bind_rows(result_df, unmatched_outs, unmatched_ins) %>%
  arrange(Date, ID, coalesce(In,Out)) %>%
  select(Date, ID, In, Out)

all.equal(result, test)
#> [1] TRUE