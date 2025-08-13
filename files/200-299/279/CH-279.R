library(tidyverse)
library(readxl)

path = "files/200-299/279/CH-279 Transforming.xlsx"
input = read_excel(path, range = "B2:C8")
test  = read_excel(path, range = "G2:H13")

result = input %>%
  mutate(prev = lag(Price)) %>%
  pivot_longer(c(prev, Price), values_to = "Price", values_drop_na = TRUE) %>%
  select(-name) 

ggplot(result, aes(Date, Price)) +
  geom_step() +
  geom_point()
ggsave("files/200-299/279/CH-279 Transforming R.png", width = 6, height = 4)

all.equal(result, test, check.attributes = FALSE)
# > [1] TRUE