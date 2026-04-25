import pandas as pd
import numpy as np

path = "400-499/402/CH-402 Matrix Normalization.xlsx"
input = pd.read_excel(path, usecols="C:F", nrows=4, skiprows=3, header=None).to_numpy()
test = pd.read_excel(path, usecols="J:M", nrows=4, skiprows=3, header=None).to_numpy()

vectorized_input = input - np.diag(input)[:, np.newaxis]
print((vectorized_input == test).all())
# True