import pandas as pd
import numpy as np

path = "300-399/360/CH-360 Matrix Calculation.xlsx"
input = pd.read_excel(path, usecols="C:H", skiprows=3, nrows=6, header=None).values
test1 = pd.read_excel(path, usecols="K:M", skiprows=3, nrows=3, header=None).values
test2 = pd.read_excel(path, usecols="P:R", skiprows=3, nrows=3, header=None).values
test3 = pd.read_excel(path, usecols="U:W", skiprows=3, nrows=3, header=None).values

def find_sym_submatrices(mat, n):
    r = []
    sz = mat.shape[0] - n + 1
    for i in range(sz):
        for j in range(sz):
            s = mat[i:i+n, j:j+n]
            if np.array_equal(s, s.T):
                r.append({'pos':(i,j), 'mat':s})
    return r

result = find_sym_submatrices(input, 3)

print((result[0]['mat'] == test1).all()) # True
print((result[3]['mat'] == test2).all()) # True
print((result[2]['mat'] == test3).all()) # True
# one extra symmetric matrix exists
print(result[1]['mat'])
# [[1 4 8]
#  [4 7 7]
#  [8 7 3]]