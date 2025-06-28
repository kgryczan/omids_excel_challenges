library(tidyverse)
library(readxl)

path = "files/200-299/256/CH-256 Table Transformation.xlsx"
input = read_excel(path, range = "B2:H6")
test  = read_excel(path, range = "B10:E14")

result = cbind(
    input[1],
    set_names(
        map_dfc(
            c("A", "B", "C"),
            ~ rowSums(input[startsWith(names(input), .x)], na.rm = TRUE)
        ),
        c("A", "B", "C")
    )
)

all.equal(result, test, check.attributes = FALSE)
# > [1] TRUE