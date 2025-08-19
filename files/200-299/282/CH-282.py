import pandas as pd
import numpy as np

path = "200-299/282/CH-282 Advanced Filtering.xlsx"
input_mat = pd.read_excel(path, engine='openpyxl', usecols="C:E", skiprows=2, nrows=8, header=None).values
test = sorted(pd.read_excel(path, engine='openpyxl', usecols="G", skiprows=2, nrows=11, header=None).squeeze().tolist())

output = np.zeros_like(input_mat, dtype=int)
for i in range(input_mat.shape[0]):
    for j in range(input_mat.shape[1]):
        if (np.sum(input_mat[i, :] == input_mat[i, j]) == 1 and
            np.sum(input_mat[:, j] == input_mat[i, j]) == 1):
            output[i, j] = 1

result = sorted(set(input_mat[output == 1].tolist()))

print(result == test) # True