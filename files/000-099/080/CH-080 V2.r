library(tidyverse)
library(readxl)

path = "files/CH-80 Convex Hulls.xlsx"
points = read_excel(path, range = "B2:C25")
test  = read_excel(path, range = "E2:F7")

lowest_point <- points[which.min(points$Y), ]
points <- points[order(points$y, points$x), ]
polar_angle <- function(p1, p2) {
  atan2(p2$Y - p1$Y, p2$X - p1$X)
}

angles <- sapply(1:nrow(points), function(i) polar_angle(lowest_point, points[i, ]))
points <- points[order(angles), ]

graham_scan <- function(points) {
  stack <- list()
  stack[[1]] <- points[1, ]
  stack[[2]] <- points[2, ]
  stack[[3]] <- points[3, ]
  for (i in 4:nrow(points)) {
    while (length(stack) >= 2 && 
           cross_product(stack[[length(stack) - 1]], stack[[length(stack)]], points[i, ]) <= 0) {
      stack <- stack[-length(stack)]
    }
    stack[[length(stack) + 1]] <- points[i, ]
  }
  do.call(rbind, stack)
}

cross_product <- function(p1, p2, p3) {
  (p2$X - p1$X) * (p3$Y - p1$Y) - (p2$Y - p1$Y) * (p3$X - p1$X)
}

hull_vertices <- graham_scan(points)
identical(hull_vertices, test)
# TRUE

# Plot the points and the convex hull
ggplot(points, aes(x = X, y = Y)) +
  geom_point() +
  geom_polygon(data = hull_vertices, aes(x = X, y = Y), color = "blue", fill = NA) +
  scale_x_continuous(breaks = seq(0, 20, 1)) +
  scale_y_continuous(breaks = seq(0, 20, 1)) +
  labs(title = "Convex Hull of Points (Manual Construction)")
