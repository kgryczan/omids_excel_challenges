import pandas as pd
import numpy as np

path = "400-499/412/CH-412 Matrix Normalization.xlsx"
input = pd.read_excel(path, usecols="C:F", nrows=4, skiprows=3, header=None).to_numpy()
test = pd.read_excel(path, usecols="J:M", nrows=4, skiprows=3, header=None).to_numpy()

result = input - np.diag(input)
print(np.array_equal(result, test))
# True