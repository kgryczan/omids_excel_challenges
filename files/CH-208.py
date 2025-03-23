import pandas as pd
import numpy as np

path = "CH-208 Matrix Calculation.xlsx"

input1 = pd.read_excel(path, usecols="C:D", skiprows=2, nrows=2, header=None).to_numpy()
input2 = pd.read_excel(path, usecols="C:E", skiprows=5, nrows=3, header=None).to_numpy()
input3 = pd.read_excel(path, usecols="C:G", skiprows=9, nrows=5, header=None).to_numpy()
test1 = pd.read_excel(path, usecols="K", skiprows=2, nrows=1, header=None).iloc[0, 0]
test2 = pd.read_excel(path, usecols="K", skiprows=5, nrows=1, header=None).iloc[0, 0]
test3 = pd.read_excel(path,  usecols="K", skiprows=9, nrows=1, header=None).iloc[0, 0]

result1 = np.trace(input1)
result2 = np.trace(input2)
result3 = np.trace(input3)

print(np.isclose(result1, test1))  # TRUE
print(np.isclose(result2, test2))  # TRUE
print(np.isclose(result3, test3))  # TRUE