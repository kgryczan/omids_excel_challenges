library(tidyverse)
library(readxl)
library(igraph)

input = read_excel("files/CH-037 Connected people.xlsx", range = "B2:C25")
test  = read_excel("files/CH-037 Connected people.xlsx", range = "E2:F6")

result = input %>%
  graph_from_data_frame(directed = FALSE) %>%
  components() %>%
  membership()  %>%
  as.data.frame() %>%
  rownames_to_column("name") %>%
  summarise(People = str_c(sort(as.numeric(name)), collapse = ","), .by = "x")

print(result)
print(test)

