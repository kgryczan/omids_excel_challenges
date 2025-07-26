library(tidyverse)
library(readxl)
library(Ryacas)
library(rootSolve)

path = "files/200-299/270/CH-270 Solving equations.xlsx"
input = read_excel(path, range = "B2:C7")
test  = read_excel(path, range = "E2:F7")

eval_lag = function(eq) yac_str(paste0("Solve(", eq, ", X)")) %>%
  y_rmvars() %>% yac_str() %>% yac_expr() %>% eval()

is_transcendental = function(eq) str_detect(eq, "\\^X")

result = input %>%
  mutate(Equation = str_replace_all(Equation, "=", "==")) %>%
  rowwise() %>%
  mutate(
    Solution = list(
      if (is_transcendental(Equation))
        uniroot.all(function(X) eval(parse(text = str_remove(Equation, "==0"))), c(-10, 10))
      else
        eval_laq(Equation)
    )
  ) %>%
  ungroup()

