library(tidyverse)
library(readxl)
library(igraph)

path = "files/CH-200People Connection.xlsx"
input = read_excel(path, range = "B2:C11")
test  = read_excel(path, range = "E2:M10")

g = graph_from_data_frame(input, directed = FALSE)
all_people = sort(unique(c(input$`Person 1`, input$`Person 2`))) 
all_com = expand.grid(a1 = all_people, a2 = all_people, stringsAsFactors = F) 

shortest_path = function(a1, a2, g){
  if (a1 == a2) {
    return("-")
  }
  path = all_shortest_paths(g, from = a1, to = a2)
  if (length(path$res) == 0 || length(path$res[[1]]$name) <= 2) {
    return("1")
  }
  nodes_between = path$res[[1]]$name[-c(1, length(path$res[[1]]$name))]
  return(paste(nodes_between, collapse = "-"))
}

result = all_com %>%
  rowwise() %>%
  mutate(path = shortest_path(a1, a2, g)) %>%
  pivot_wider(names_from = a1, values_from = path)

print(result)
print(test)

# Discrepancies because of incosistent node sorting, but the paths are correct