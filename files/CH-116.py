import pandas as pd
import numpy as np

path = "CH-116 Remove rows and colums.xlsx"
input = pd.read_excel(path, usecols="C:H", skiprows = 1, nrows = 7).to_numpy()
test = pd.read_excel(path, usecols="K:M", skiprows = 1, nrows = 3).to_numpy()
result = input[::2,::2]

print(np.array_equal(result, test)) # True