library(clue)

M = matrix(c(13,	4,	7,	6, 1,	11,	5,	4, 6,	7,	2,	8, 1,	3,	5, 9), nrow = 4, byrow = TRUE)

result = solve_LSAP(M)
result

# Optimal assignment:
#   1 => 2, 2 => 4, 3 => 3, 4 => 1
# 
# # it is Task => Person