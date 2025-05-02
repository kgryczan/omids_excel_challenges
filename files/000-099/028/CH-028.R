library(tidyverse)
library(readxl)
library(igraph)

input = read_excel("files/CH-028 Cluster values.xlsx", range = "B1:B16")
test  = read_excel("files/CH-028 Cluster values.xlsx", range = "E2:F6") %>%
  mutate(Values = map(Values, ~strsplit(., ",") %>% unlist() %>% as.numeric() %>% 
                        sort() %>% paste(collapse = ","))) %>%
  select(Values) %>%
  pull()

edges <- input$`Question Tables` %>%
  strsplit(",") %>%
  map(~combn(.x, 2, simplify = TRUE) %>% t()) %>% 
  do.call(rbind, .) %>% 
  as.data.frame(stringsAsFactors = FALSE)

graph <- graph_from_data_frame(edges, directed = FALSE)
components <- components(graph)$membership

result <- unique(components) %>%
  map(~{
    ids <- names(components[components == .x])
    paste(sort(as.numeric(ids)), collapse = ",")
  })

identical(result, test)
# [1] TRUE

plot(graph)
