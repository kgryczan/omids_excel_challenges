library(tidyverse)
library(readxl)

path <- "400-499/435/CH-435 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:E6")
test <- read_excel(path, range = "G3:J12")

result <- input %>%
  pivot_longer(cols = -Column1, names_to = "Variable", values_to = "Value") %>%
  na.omit() %>%
  separate_wider_delim(Value, delim = "},{", names = c("Value1", "Value2")) %>%
  mutate(across(c(Value1, Value2), ~ str_remove_all(.x, "[\\{\\}]"))) %>%
  separate_longer_delim(c(Value1, Value2), delim = ",") %>%
  select(
    DATE = Column1,
    CUSTOMER = Variable,
    PRODUCT = Value1,
    SALES = Value2
  ) %>%
  mutate(SALES = as.numeric(SALES))

all.equal(result, test)
# TRUE
