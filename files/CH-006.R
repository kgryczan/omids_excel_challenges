library(tidyvverse)
library(readxl)
library(FNN)

path = "files/CH-006.xlsx"
input = read_excel(path, range = "B2:B12")

# conduct knn with n = 2 on input values and put cluster number in column C, then n = 3 into D, and n = 4 into E

output = input %>%
  mutate(C = kmeans(input, centers = 2)$cluster,
         D = kmeans(input, centers = 3)$cluster,
         E = kmeans(input, centers = 4)$cluster)
