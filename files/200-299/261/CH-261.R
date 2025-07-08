library(tidyverse)
library(readxl)

path = "files/200-299/261/CH-261 Custom Grouping .xlsx"
input = read_excel(path, range = "B2:C16")
test  = read_excel(path, range = "F2:H16")

group = 1
seen = character()

result = input %>% mutate(
  Group = map_int(ID, ~{
    if (.x %in% seen) {
      group <<- group + 1
      seen <<- .x
    } else {
      seen <<- c(seen, .x)
    }
    group
  })
)

all.equal(result, test)
# > [1] TRUE