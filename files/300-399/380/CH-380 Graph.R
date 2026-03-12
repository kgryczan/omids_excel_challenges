library(tidyverse)
library(readxl)
library(igraph)

path <- "300-399/380/CH-380 Matrix Calculation.xlsx"
input <- read_excel(path, range = "B3:G8")
test <- read_excel(path, range = "J3:K8")

edges = input %>%
  pivot_longer(-Edge, names_to = "to", values_to = "value") %>%
  filter(value == 1) %>%
  transmute(from = Edge, to)

g <- graph_from_data_frame(edges, directed = TRUE)

result = topo_sort(g, mode = "out") |>
  as_ids() %>%
  data.frame(Factor = .) %>%
  mutate(Rank = row_number(), .before = 1)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
