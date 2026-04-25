library(tidyverse)
library(readxl)

path <- "400-499/400/CH-400 Rook Polynomial.xlsx"
input <- read_excel(path, range = "B3:J11") %>% column_to_rownames(var = "row")
test <- read_excel(path, range = "L3:L9")

rook_locations <- which(!is.na(input), arr.ind = TRUE)
rook_positions <- data.frame(
  row = as.numeric(rownames(input)[rook_locations[, 1]]),
  col = colnames(input)[rook_locations[, 2]]
)
free_cols <- setdiff(letters[1:8], rook_positions$col)
free_rows <- setdiff(1:8, rook_positions$row)
result = data.frame(x = free_cols, y = free_rows) %>%
  unite("Locations", x, y, sep = "")
all.equal(result$Locations, test$Locations, check.attributes = FALSE)
# [1] TRUE
