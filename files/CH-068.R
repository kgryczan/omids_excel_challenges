library(tidyverse)

draw_triangle = function(n) {
  if (n %% 2 == 0) {
    return("Not Possible")
  } else {
    x = ceiling(n / 2)
    seq = seq(1, x)
    
    mat = matrix("", n, x)
    for (i in 1:x) {
      mat[i, 1:seq[i]] = "*"
    }
    for (i in 1:(x - 1)) {
      mat[n - i + 1, ] = mat[i, ]
    }
    
    print(mat)
  }
}


draw_triangle(7)
