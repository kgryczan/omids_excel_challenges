import pandas as pd
import numpy as np

def place_knights_pattern(start_row=1, start_col=1):
    columns = np.arange(8)
    rows = ((start_row - 1 + columns - (start_col - 1)) % 8)
    board = np.full((8, 8), "", dtype=object)
    board[rows, columns] = "K"
    return pd.DataFrame(board)

print(place_knights_pattern(0, 5))

#    0  1  2  3  4  5  6  7
# 0                 K      
# 1                    K   
# 2                       K
# 3  K
# 4     K
# 5        K
# 6           K
# 7              K