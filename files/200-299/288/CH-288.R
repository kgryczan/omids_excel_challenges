library(tidyverse)
library(readxl)

path = "files/200-299/288/CH-288 Transforming.xlsx"
input = read_excel(path, range = "B2:C11")
test  = read_excel(path, range = "G2:H7")

result = input %>%
  mutate(Product = ifelse(Price >= 10, Product, "Other")) %>%
  summarise(Price = sum(Price, na.rm = TRUE), .by = Product) %>%
  arrange(desc(Price))

all.equal(result, test)
# > [1] TRUE

ggplot(result, aes(x = "", y = Price, fill = Product)) +
  geom_bar(stat = "identity", width = 1) +
  coord_polar("y", start = 0) +
  theme_void() +
  labs(title = "Price Distribution by Product") +
  theme(legend.title = element_blank())
