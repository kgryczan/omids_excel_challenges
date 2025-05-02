library(tidyverse)
library(readxl)
library(combinat)

path = "files/CH-110-Reconciliation .xlsx"
input1 = read_excel(path, range = "B2:D7")
input2 = read_excel(path, range = "F2:H9")
test   = read_excel(path, range = "J2:J8")


generate_combinations_with_cumsum <- function(financial_values, financial_ids) {
  n <- length(financial_values)
  all_combinations <- list()
  for (i in 1:n) {
    comb <- combn(n, i, simplify = FALSE)
    for (subset_idx in comb) {
      subset_vals <- financial_values[subset_idx]
      subset_ids <- financial_ids[subset_idx]
      cumsum_vals <- cumsum(subset_vals)
      all_combinations[[length(all_combinations) + 1]] <- data.frame(IDs = paste(subset_ids, collapse = ", "),
                                                                     Values = paste(subset_vals, collapse = ", "),
                                                                     CumSum = cumsum_vals[length(cumsum_vals)])
    }
  }
  return(do.call(rbind, all_combinations))
}

financial_combinations <- generate_combinations_with_cumsum(input2$Value, input2$ID)
bank_combinations <- generate_combinations_with_cumsum(input1$Value, input1$ID)

match_combinations <- function(target_data, combination_data, match_col) {
  matched <- list()
  for (i in 1:nrow(target_data)) {
    target_value <- target_data$Value[i]
    target_id <- target_data$ID[i]

    matching_combinations <- combination_data[combination_data[[match_col]] == target_value, ]

    if (nrow(matching_combinations) > 0) {
      matched[[target_id]] <- matching_combinations
    }
  }
  return(matched)
}

forward_matches <- match_combinations(input1, financial_combinations, "CumSum")
backward_matches <- match_combinations(input2, bank_combinations, "CumSum")

all = bind_rows(
enframe(backward_matches) %>% unnest(value), 
enframe(forward_matches) %>% unnest(value) 
)

all1 = all %>% 
  mutate(bank_id = ifelse(str_detect(name, "B"), name, IDs),
         fin_id = ifelse(str_detect(name, "F"), name, IDs),
         value = as.numeric(str_extract(CumSum, "\\d+"))) %>%
  select(bank_id, fin_id, value) %>%
  distinct() 

split_ids <- function(ids) {
  unlist(strsplit(ids, ", "))
}

all_bank_ids <- c("B1", "B2", "B3", "B4", "B5")
all_fin_ids <- c("F1", "F2", "F3", "F4", "F5", "F6", "F7")

check_coverage <- function(subset) {
  bank_ids <- unlist(lapply(subset$bank_id, split_ids)) 
  fin_ids <- unlist(lapply(subset$fin_id, split_ids)) 
  
  all(all_bank_ids %in% bank_ids) && all(all_fin_ids %in% fin_ids) &&
    length(bank_ids) == length(unique(bank_ids)) && 
    length(fin_ids) == length(unique(fin_ids))
}

subset_combinations <- function(data) {
  n <- nrow(data)
  combinations <- list()
  
  for (i in 1:n) {
    comb <- combn(n, i, simplify = FALSE)
    for (idx in comb) {
      combinations[[length(combinations) + 1]] <- data[idx, ]
    }
  }
  return(combinations)
}

all_combinations <- subset_combinations(all1)
valid_combinations <- lapply(all_combinations, function(subset) {
  if (check_coverage(subset)) {
    return(subset)
  } else {
    return(NULL)
  }
})

valid_combinations <- valid_combinations[!sapply(valid_combinations, is.null)]
nested_combinations <- tibble(
  comb_id = seq_along(valid_combinations),
  data = valid_combinations
)

result = nested_combinations %>%
  mutate(data = map(data, ~unite(., "bank_fin_id", bank_id, fin_id, sep = "="))) %>%
  mutate(data = map(data, ~mutate(., bank_fin_id = str_replace_all(bank_fin_id, ", ", "+")))) %>%
  unnest(data) %>%
  summarize(Scenarios = paste(sort(bank_fin_id), collapse = ", "), .by = comb_id) %>%
  arrange(Scenarios)

identical(result$Scenarios, test$Senarios)
# [1] TRUE