library(tidyverse)
library(readxl)
library(criticalpath)

path = "files/CH-220 Project Critical path.xlsx"
df = read_excel(path, range = "B3:D11", col_names = c("id", "duration", "pred"))
test = read_excel(path, range = "F2:F3")

df <- df %>% mutate(id = as.integer(id), duration = as.integer(duration))

relations <- df %>%
  drop_na(pred) %>%
  separate_rows(pred, sep = ",") %>%
  transmute(from = as.integer(pred), to = id) %>%
  na.omit()

sch <- sch_new() %>%
  sch_add_activities(id = df$id, name = paste0("Task ", df$id), duration = df$duration) %>%
  sch_add_relations(from = relations$from, to = relations$to) %>%
  sch_plan()

result = sch_critical_activities(sch) %>%
  select(id) %>%
  summarise(critical_path = paste(id, collapse = ","))
result

# 1,2,4,6,8,9