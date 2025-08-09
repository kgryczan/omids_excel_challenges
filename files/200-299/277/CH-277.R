library(tidyverse)
library(readxl)

path = "files/200-299/277/CH-277 Noise Removing.xlsx"
input = read_excel(path, range = "B2:D17")

## first solution - easy way (special library)
library(cluster)

dist_matrix = dist(input[,c("X", "Y")], method = "euclidean")
dist_df = as.matrix(dist_matrix)
neighbor_counts = apply(dist_df, 1, function(x) sum(x < 3) - 1) 
input$Neighbors = neighbor_counts
input$Is_Noise = neighbor_counts <= 2

noise_points = input$ID[input$Is_Noise]
print(noise_points)

# Plotting
library(ggforce)

input$Noise_Label = ifelse(input$Is_Noise, as.character(input$ID), NA)

circle_df = input %>%
  filter(Is_Noise) %>%
  mutate(r = 0.7, 
         facet_id = as.character(ID)) %>%
  select(facet_id, X, Y, r)

facet_input = input %>%
  filter(TRUE) %>%
  crossing(facet_id = as.character(noise_points))

facet_input = facet_input %>%
  mutate(is_this_noise = ID == facet_id)

p = ggplot(facet_input, aes(x = X, y = Y)) +
  geom_point(size = 1) +
  geom_point(data = subset(facet_input, is_this_noise), color = "red", size = 1) +
  ggforce::geom_circle(data = circle_df, aes(x0 = X, y0 = Y, r = 3), 
                       color = "blue", fill = NA, inherit.aes = FALSE) +
  facet_wrap(~facet_id, nrow = 1) +
  theme_minimal() +
  coord_fixed() +
  labs(title = "Noise Points Highlighted", subtitle = "Each facet highlights one noise point")
  
print(p)

## second solution - math (no special library)
input2 = read_excel(path, range = "B2:D17")
noise_points_math = input2 %>%
  mutate(
    neighbors = map_int(ID, ~ {
      current_point = input2[input2$ID == .x, ]
      other_points = input2[input2$ID != .x, ]
      
      distances_sq = (current_point$X - other_points$X)^2 + 
        (current_point$Y - other_points$Y)^2
      sum(distances_sq <= 9)
    }),
    is_noise = neighbors <= 2) %>%
  filter(is_noise) %>%
  pull(ID)

print(noise_points_math)
