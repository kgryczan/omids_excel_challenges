import numpy as np
import pandas as pd

p = "400-499/452/CH-452 Matrix Normalization.xlsx"
matrix = pd.read_excel(p, sheet_name="Sheet1", header=None).iloc[3:7, 2:6].to_numpy()
expected = pd.read_excel(p, sheet_name="Sheet1", header=None).iloc[3:7, 9:13].to_numpy()

result = np.sort(np.sort(matrix, axis=1), axis=0)
print((result == expected).all())
