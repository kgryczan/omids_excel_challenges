import numpy as np
import pandas as pd

path = "300-399/344/CH-344  Matrix Calculation.xlsx"

input1 = pd.read_excel(path, usecols="B:F", skiprows=3, nrows=5, header=None).values
input2 = pd.read_excel(path, usecols="B:F", skiprows=13, nrows=5, header=None).values
test1 = pd.read_excel(path, usecols="H", skiprows=3, nrows=1, header=None).iloc[0,0]
test2 = pd.read_excel(path, usecols="H", skiprows=13, nrows=1, header=None).iloc[0,0]

def is_symmetric(mat):
    return np.all(mat == mat.T)

max_sym1 = max([x for x in range(1, min(input1.shape)+1) if is_symmetric(input1[:x, :x])])
max_sym2 = max([x for x in range(1, min(input2.shape)+1) if is_symmetric(input2[:x, :x])])

print(np.isclose(test1, max_sym1))  # True
print(np.isclose(test2, max_sym2))  # True
