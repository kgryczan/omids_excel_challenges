library(tidyverse)
library(readxl)
library(igraph)

path <- "300-399/355/CH-355 Graph Calculation.xlsx"
input1 <- read_excel(path, range = "B3:H9")
input2 <- read_excel(path, range = "K3:L7")
test <- read_excel(path, range = "M3:M7")

i1 = input1 %>%
  pivot_longer(cols = -Edge, names_to = "To", values_to = "Dist") %>%
  na.omit()

g = graph_from_data_frame(i1, directed = TRUE)

define_shortest_path <- function(g, from_node, to_node) {
  shortest_path <- shortest_paths(
    g,
    from = from_node,
    to = to_node,
    weights = E(g)$Dist,
    output = "vpath"
  )
  shortest_path_nodes <- shortest_path$vpath[[1]] %>%
    as_ids() %>%
    paste0(collapse = ",")
  return(shortest_path_nodes)
}

result = input2 %>%
  mutate(result = map2_chr(From, To, ~ define_shortest_path(g, .x, .y)))

all.equal(result$result, test$`Shortest Path`)
# [1] TRUE
