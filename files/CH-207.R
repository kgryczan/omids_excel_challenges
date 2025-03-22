library(tidyverse)
library(readxl)

path = "files/CH-207 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C18")
test  = read_excel(path, range = "B2:D18")

initial_threshold <- 100
threshold_step <- 50

result = input %>%
  mutate(
    Group = accumulate(
      Sales,
      .init = list(total = 0, Group = 1),
      .f = function(acc, x) {
        threshold <- initial_threshold + (acc$Group - 1) * threshold_step
        if (acc$total + x > threshold) {
          list(total = x, Group = acc$Group + 1)
        } else {
          list(total = acc$total + x, Group = acc$Group)
        }
      }
    )[-1] %>%
      map_int("Group")
  )

all.equal(result, test)
#> [1] TRUE
