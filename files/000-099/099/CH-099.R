library(tidyverse)
library(readxl)

path = 'files/CH-099 Random Selection Part 2.xlsx'
input = read_excel(path, range = "B2:C20")

sample_dept_and_emp <- function(input,n) {
  n = 4
  n_distinct = n_distinct(input$Department)
  emp_per_dept = input %>% count(Department) 
  
  repeat {
    sampled_departments = sample(unique(input$Department), n, 
                                 replace = TRUE, 
                                 prob = rep(1/n_distinct, n_distinct)) %>%
      tibble(Department = .) %>%
      mutate(nr = row_number(), .by = Department) %>%
      slice_max(nr, by = Department)
    check = sampled_departments %>% 
      left_join(emp_per_dept, by = c("Department"))
    if (all(check$n >= check$nr)) {
      break
    }
  }
  
  sampled_employees = input %>%
    left_join(sampled_departments, by = "Department") %>%
    na.omit() %>%
    nest_by(Department, nr) %>%
    mutate(data = list(sample_n(data, nr, replace = F))) %>%
    unnest(data) %>%
    ungroup() %>%
    select(-nr)

  return(sampled_employees)
}

sample_dept_and_emp(input, 4)

# # A tibble: 4 × 2
#   Department `Staff ID`
#   <chr>      <chr>     
# 1 Marketing  S_03      
# 2 Production S_18      
# 3 Production S_16      
# 4 Production S_05    

# # A tibble: 4 × 2
#   Department `Staff ID`
#   <chr>      <chr>     
# 1 IT         S_04      
# 2 Marketing  S_02      
# 3 R&D        S_15      
# 4 R&D        S_13 

