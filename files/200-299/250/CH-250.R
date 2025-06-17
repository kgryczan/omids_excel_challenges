library(tidyverse)
library(readxl)


path = "files/200-299/250/CH-250  Hierarchical Structure from ID Codes.xlsx"
input = read_excel(path, range = "B2:C10")
test = read_excel(path, range = "E2:H6")

lookup = deframe(input)

get_path = function(id, path = c()) {
  parent = lookup[as.character(id)]
  if (is.na(parent)) {
    return(c(id, path))
  } else {
    get_path(parent, c(id, path))
  }
}

leaves = setdiff(input$ID, input$ParentID)

paths = map(leaves, get_path)

max_len = max(lengths(paths))
paths_df = paths %>%
  map(~ c(.x, rep(NA_integer_, max_len - length(.x)))) %>%
  map_dfr(~ set_names(as.list(.x), paste0("Level ", seq_along(.x))))

# different outcome than expected.
