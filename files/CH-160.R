place_knights = function(start_row = 1, start_col = 1) {
  startY = start_row - 1
  startX = start_col - 1
  columns = 0:7
  rows = ((startY + columns - startX) %% 8) + 1
  board = matrix("", nrow = 8, ncol = 8)
  board[cbind(rows, columns + 1)] = "K"
  as.data.frame(board, stringsAsFactors = FALSE)
}

place_knights_pattern(2,6)

#   V1 V2 V3 V4 V5 V6 V7 V8
# 1              K         
# 2                 K      
# 3                    K   
# 4                       K
# 5  K                     
# 6     K                  
# 7        K               
# 8           K            