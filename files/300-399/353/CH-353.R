library(readxl)

path <- "300-399/353/CH-353 Appending.xlsx"
input1 <- read_excel(path, range = "B3:E6")
input2 <- read_excel(path, range = "B9:E12")
test <- read_excel(path, range = "G3:J9")

semantic_type <- function(x) {
  if (inherits(x, "POSIXct")) {
    if (all(as.Date(x) == as.Date("1899-12-31"))) "time" else "date"
  } else if (is.character(x)) {
    "character"
  } else if (is.numeric(x)) {
    "numeric"
  } else {
    "other"
  }
}

append_by_semantic_type <- function(base, new) {
  bt <- purrr::map_chr(base, semantic_type)
  nt <- purrr::map_chr(new, semantic_type)
  if (!setequal(bt, nt)) {
    stop("Semantic type mismatch")
  }
  new2 <- purrr::map_dfc(bt, ~ new[which(nt == .x)])
  colnames(new2) <- colnames(base)
  dplyr::bind_rows(base, new2)
}

result <- append_by_semantic_type(input1, input2)
all.equal(result, test)
