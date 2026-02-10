import pandas as pd
import numpy as np
path = "300-399/365/CH-365 Matrix Calculation.xlsx"

input = pd.read_excel(path, usecols="C:G", skiprows=3, nrows=4, header=None).to_numpy()
test = pd.read_excel(path, usecols="K:O", skiprows=3, nrows=4, header=None).to_numpy()

def add_surrounding(mat):
    result = np.zeros_like(mat)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            rows = slice(max(0, i - 1), min(mat.shape[0], i + 2))
            cols = slice(max(0, j - 1), min(mat.shape[1], j + 2))
            result[i, j] = np.sum(mat[rows, cols]) - mat[i, j]
    return result
result = add_surrounding(input)

comparison = np.allclose(result, test, equal_nan=True)
print(comparison) # True