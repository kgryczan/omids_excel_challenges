library(tidyverse)
library(readxl)

path = "files/200-299/229/CH-229 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:B102")
mean = 463

give_range = function(df, mean, perc) {
  d = df %>%
    mutate(dist = abs(. - mean)) %>%
    arrange(dist) %>%
    slice(ceiling(n() * perc)) %>%
    pull()
  return(paste0(mean - d, "-", mean + d))
}

result = tibble(pc = seq(0.1, 1, 0.1)) %>%
  mutate(Range = map_chr(pc, ~ give_range(input, mean, .)))
