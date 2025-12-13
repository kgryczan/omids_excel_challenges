library(tidyverse)
library(readxl)

path <- "300-399/340/CH-340 Table Transformation.xlsx"
input <- read_excel(path, range = "B3:G10")
test <- read_excel(path, range = "K3:N8")

remove_L <- function(df) {
  t(apply(df, 1, function(row) {
    vals <- row[row != "L"]
    c(vals, rep(NA, length(row) - length(vals)))
  }))
}
remove_U <- function(df) {
  as.data.frame(lapply(df, function(col) {
    vals <- col[col != "U"]
    c(vals, rep(NA, length(col) - length(vals)))
  }))
}
clean_result <- function(df) {
  df <- df[, colSums(is.na(df)) < nrow(df), drop = FALSE]
  colnames(df) <- c("Date", "Product", "Customer", "Quantity")
  df <- df[complete.cases(df), ]
  return(df)
}

result = input %>%
  remove_L() %>%
  as.data.frame() %>%
  remove_U() %>%
  clean_result() %>%
  mutate(
    Date = as.numeric(Date) %>%
      janitor::excel_numeric_to_date(.) %>%
      as.POSIXct(),
    Quantity = as.numeric(Quantity)
  )

all.equal(result, test, check.attributes = FALSE)
