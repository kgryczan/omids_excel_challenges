import pandas as pd
import numpy as np

path = "300-399/370/CH-370 Matrix Calculation.xlsx"
mat = pd.read_excel(path, sheet_name=0, usecols="C:G", skiprows=3, nrows=4, header=None).to_numpy()

def find_submatrices(mat, target):
    mat = np.array(mat)
    n_rows, n_cols = mat.shape
    submatrices = []

    for start_row in range(n_rows):
        for start_col in range(n_cols):
            for end_row in range(start_row, n_rows):
                for end_col in range(start_col, n_cols):
                    submatrix = mat[start_row:end_row+1, start_col:end_col+1]
                    if submatrix.sum() == target:
                        submatrices.append(submatrix)

    return submatrices

target_sum = 16
result = find_submatrices(mat, target_sum)
print(result)