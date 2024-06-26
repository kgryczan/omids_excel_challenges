library(tidyverse)
library(readxl)

input = read_excel("files/CH-050 Assignment Problem Part 2.xlsx", range = "B2:F6") 
input = column_to_rownames(input, var = "...1")
input = as.matrix(input)

test = read_excel("files/CH-050 Assignment Problem Part 2.xlsx", range = "AK2:AL6")
test = test %>%
  arrange(Person)


library(R6)

CoveredMatrix <- R6::R6Class(
  "CoveredMatrix",
  public = list(
    data = NULL,
    covered = NULL,

    initialize = function(nrow = 1, ncol = 1) {
      self$data <- matrix(0, nrow = nrow, ncol = ncol)
      self$covered <- matrix(0, nrow = nrow, ncol = ncol)
    },

    print = function() {
      cat("Data Matrix:\n")
      print(self$data)
      cat("Covered Matrix:\n")
      print(self$covered)
    },

    mark_covered = function(row = NULL, col = NULL) {
      if (!is.null(row) && !is.null(col)) {
        self$covered[row, col] <- self$covered[row, col] + 1
      } else if (!is.null(row)) {
        self$covered[row, ] <- self$covered[row, ] + 1
      } else if (!is.null(col)) {
        self$covered[, col] <- self$covered[, col] + 1
      } else {
        stop("Either row or column must be specified")
      }
    },

    uncover = function(row = NULL, col = NULL) {
      if (!is.null(row) && !is.null(col)) {
        self$covered[row, col] <- max(0, self$covered[row, col] - 1)
      } else if (!is.null(row)) {
        self$covered[row, ] <- pmax(0, self$covered[row, ] - 1)
      } else if (!is.null(col)) {
        self$covered[, col] <- pmax(0, self$covered[, col] - 1)
      } else {
        stop("Either row or column must be specified")
      }
    }
  )
)

# find row with max number of zeros using method from class above

input_matrix = CoveredMatrix$new(nrow(input), ncol(input))
input_matrix$data = input

input_matrix$print()

# find number of zeroes per row and col
zeroes_per_row = apply(input_matrix$data, 1, function(x) sum(x == 0))
zeroes_per_col = apply(input_matrix$data, 2, function(x) sum(x == 0))

# cover row and col with max number of zeroes
row_to_cover = which.max(zeroes_per_row)
col_to_cover = which.max(zeroes_per_col)

input_matrix$mark_covered(row = row_to_cover)
input_matrix$mark_covered(col = col_to_cover)

input_matrix$print()

# find all uncovered zeroes
uncovered_zeroes = which(input_matrix$data == 0 & input_matrix$covered == 0, arr.ind = TRUE)

# cover col with uncovered zero
col_to_cover = uncovered_zeroes[1, "col"]
input_matrix$mark_covered(col = col_to_cover)
input_matrix$print()

# identify uncovered cells
uncovered_cells = which(input_matrix$covered == 0, arr.ind = TRUE)
# find minimum value in uncovered cells
min_val = min(input_matrix$data[uncovered_cells])
# subtract min value from all uncovered cells
input_matrix$data[uncovered_cells] = input_matrix$data[uncovered_cells] - min_val

# add min value to all cells covered by two lines
covered_cells = which(input_matrix$covered == 2, arr.ind = TRUE)
input_matrix$data[covered_cells] = input_matrix$data[covered_cells] + min_val

input_matrix$print()

# count number of lines

row_lines = sum(apply(input_matrix$covered, 1, function(x) any(x == 2)))
col_lines = sum(apply(input_matrix$covered, 2, function(x) any(x == 2)))

all_lines = row_lines + col_lines

# treat input_matrix as new input
input_matrix2 = CoveredMatrix$new(nrow(input_matrix$data), ncol(input_matrix$data))
input_matrix2$data = input_matrix$data

input_matrix2$print()

# find rows with zeroes 
rows_with_zeroes = apply(input_matrix2$data, 1, function(x) any(x == 0))
cols_with_zeroes = apply(input_matrix2$data, 2, function(x) any(x == 0))

# cover rows with zeroes
rows_to_cover = which(rows_with_zeroes)
                      
input_matrix2$mark_covered(row = rows_to_cover)                      
input_matrix2$print()

# step 6 
# get cells with zeroes

zeroes = which(input_matrix2$data == 0, arr.ind = TRUE)
input_matrix2$covered = input_matrix2$covered - 1
input_matrix2$print()

# cover cells with zeroes unique per row
rows = unique(zeroes[, "row"])
cols = unique(zeroes[, "col"])

for (i in 1:length(rows)) {
  row = rows[i]
  row_zeroes = zeroes[zeroes[, "row"] == row, "col"]
  if (length(row_zeroes) == 1) {
    input_matrix2$mark_covered(row = row, col = row_zeroes)
  }
}

input_matrix2$print()

# get column with zero and with no covered cells
cols_with_zeroes = apply(input_matrix2$data, 2, function(x) any(x == 0))
cols_with_no_covered = apply(input_matrix2$covered, 2, function(x) all(x == 0))

cols_to_cover = which(cols_with_zeroes & cols_with_no_covered)
# get first
col_to_cover = cols_to_cover[1]

# cover cell in column col_to_cover, which has zero but no zero another zero in row
col_zeroes = zeroes[zeroes[, "col"] == col_to_cover, "row"]
row_to_cover = col_zeroes[1]

input_matrix2$mark_covered(row = row_to_cover, col = col_to_cover)
input_matrix2$print()

# check if there is row and col with no covered cells, if yes check if there is zero in cell and cover it
rows_with_no_covered = apply(input_matrix2$covered, 1, function(x) all(x == 0))
cols_with_no_covered = apply(input_matrix2$covered, 2, function(x) all(x == 0))

if (any(rows_with_no_covered) && any(cols_with_no_covered)) {
  row_to_cover = which(rows_with_no_covered)[1]
  col_to_cover = which(cols_with_no_covered)[1]
  
  if (input_matrix2$data[row_to_cover, col_to_cover] == 0) {
    input_matrix2$mark_covered(row = row_to_cover, col = col_to_cover)
  }
}

input_matrix2$print()

# extract covered matrix and to get final result
result = input_matrix2$covered
colnames(result) = colnames(input)
rownames(result) = rownames(input)

result2 = result %>%
  as.data.frame() %>%
  mutate(row = rownames(.)) %>%
  pivot_longer(-row, names_to = "col", values_to = "value") %>%
  filter(value == 1) %>%
  select(-value) %>%
  select(Person = col,Tasks = row) %>%
  arrange(Tasks)

all.equal(result2, test, check.attributes = FALSE)
# [1] TRUE