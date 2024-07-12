library(tidyverse)
library(readxl)


path = "files/CH-081 Compaint grouping.xlsx"
input1 = read_xlsx(path, range = "B2:F6")
input2 = read_xlsx(path, range = "H2:J14")
test  = read_xlsx(path, range = "K2:K14")

result1 = input1 %>%
  pivot_longer(cols = -c(`From-To`), names_to = "To", values_to = "Distance")

result2 = input2 %>%
  separate_rows(Path, sep = ",") %>%
  mutate(to = lead(Path), .by = c(Date, `Staff ID`)) %>%
  na.omit()

result = result2 %>%
  left_join(result1, by = c("Path" = "From-To", "to" = "To")) %>%
  summarise(Distance = sum(Distance, na.rm = TRUE), .by = c(Date, `Staff ID`))

identical(result$Distance, test$Distance)
#> [1] TRUE