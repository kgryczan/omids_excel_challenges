library(tidyverse)
library(readxl)
library(patchwork)

path = "files/CH-80 Convex Hulls.xlsx"
input = read_excel(path, range = "B2:C25")
test  = read_excel(path, range = "E2:F7")

hull_indices = chull(input$X, input$Y)
hull_vertices = input[hull_indices,]
hull_vertices = rbind(hull_vertices, hull_vertices[1,])


# code for plot ----
CH = ggplot(input, aes(x = X, y = Y)) +
  geom_point() +
  geom_polygon(data = hull_vertices, aes(x = X, y = Y), fill = "blue", alpha = 0.2) +
  scale_x_continuous(breaks = seq(0, 20, 1)) +
  scale_y_continuous(breaks = seq(0, 20, 1)) +
  labs(title = "Convex Hull of Points")

P = ggplot(input, aes(x = X, y = Y)) +
  geom_point() +
  scale_x_continuous(breaks = seq(0, 20, 1)) +
  scale_y_continuous(breaks = seq(0, 20, 1)) +
  labs(title = "Points")

P + CH

# validation ----
hull_vertices_val = hull_vertices %>% distinct() %>% arrange(X, Y)
test = test %>% arrange(X, Y)

identical(hull_vertices_val, test)
#> [1] TRUE
