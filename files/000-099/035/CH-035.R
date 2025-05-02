library(tidyverse)
library(readxl)

input = read_excel("files/CH-035 Up and Down Grades.xlsx", range = "B2:D37")
test  = read_excel("files/CH-035 Up and Down Grades.xlsx", range = "H2:K6")

result = input %>%
  mutate(month = floor_date(Date, "month"),
         Grade = factor(Grade, levels = c("A+","A", "B", "C"), ordered = TRUE)) %>%
  summarise(last_grade = last(Grade), .by = c(`Agent-id`, month)) %>%
  arrange(`Agent-id`, month) %>%
  mutate(prev_grade = lag(last_grade), .by = `Agent-id`) %>%
  filter(!is.na(prev_grade)) %>%
  mutate(transition = case_when(
    prev_grade > last_grade ~ "Upgrade",
    prev_grade < last_grade ~ "Down-grade",
    TRUE ~ "No change"
  )) %>%
  mutate(month = as.numeric(factor(month))) %>%
  summarise(transitions = n(), .by = c(transition, month)) %>%
  pivot_wider(names_from = transition, values_from = transitions, values_fill = 0) %>%
  arrange(month) %>%
  select(Month = month, Upgrade, `No change`, `Down-grade`)

print(result)
print(test)

  