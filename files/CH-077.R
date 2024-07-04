library(tidyverse)
library(readxl)

path = "files/CH-77 Character-Based Rhombus.xlsx"
test = read_xlsx(path, range = "C2:Q16", col_names = FALSE) %>%
  map_df(~replace_na(.x, "_")) %>%
  unite("rhombus", everything(), sep = "")

draw_rhombus = function(diag) {
  if (diag %% 2 == 0) {
    stop("diag must be an odd number")
  }
  
  rhombus = matrix(NA, nrow = diag, ncol = diag)
  seq = seq(1, diag, by = 2)
  rev_seq = rev(seq)[-1] 
  seq = c(seq, rev_seq)
  
  for (i in 1:diag) {
    rhombus[i, 1:seq[i]] = "*"
  }
  
  rhombus = as_tibble(rhombus) %>%
    mutate_all(as.character) %>%
    unite("rhombus", everything(), sep = "", na.rm = TRUE) %>%
    mutate(rhombus = str_pad(rhombus, diag, side = "both", pad = "_"))
  
  return(rhombus)
}

result = draw_rhombus(15)

identical(result, test)
#> [1] TRUE