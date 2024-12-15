library(tidyverse)
library(readxl)

path = "files/CH-159 Data Cleaning.xlsx"
input = read_excel(path, range = "C2:I27")
test  = read_excel(path, range = "K2:N6")

result = input %>%
  pivot_longer(-Date, names_to = "Sensor", values_to = "Temperature") %>%
  arrange(Sensor, Date) %>%
  mutate(group = cumsum(lag(Temperature, default = first(Temperature)) != Temperature), .by = Sensor) %>%
  mutate(length = n(), .by = c(Sensor, group)) %>%
  filter(length >= 4) %>%
  summarise(From = min(Date), TO = max(Date), Temperature = first(Temperature), Sensor = first(Sensor), .by = group) %>%
  select(From, TO, Sensor, Temperature)

all.equal(result, test)
#> [1] TRUE