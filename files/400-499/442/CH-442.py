import pandas as pd
import numpy as np

path = "400-499/442/CH-442 Matrix Normalization.xlsx"
input = pd.read_excel(path, usecols="C:F", nrows=4, skiprows=3, header=None).to_numpy()
test = pd.read_excel(path, usecols="J:M", nrows=4, skiprows=3, header=None).to_numpy()

diag = np.diag(input)
value_range = np.diag(input).max() - np.diag(input).min()
result = input / value_range

print((result == test).all())
# True
