library(tidyverse)
library(readxl)

path = "files/200-299/297/CH-297 Custom Grouping.xlsx"
input = read_excel(path, range = "B2:C19")
test  = read_excel(path, range = "G2:H8")

give_triangular = function(x) {
  k = ceiling((sqrt(8 * x + 1) - 1) / 2)
  k * (k + 1) / 2
}
t = give_triangular(nrow(input))
seq = rep(1:t, times = 1:t)[1:nrow(input)] 

result = input %>%
  mutate(Group = seq) %>%
  summarise(`Total Sales` = sum(Sales), .by = Group)

all.equal(result, test)
# [1] TRUE