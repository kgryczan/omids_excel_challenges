import pandas as pd
import numpy as np

path = "CH-151 Solid Worl.xlsx"

input = pd.read_excel(path, usecols="B:F", skiprows=1, nrows=8).to_numpy().flatten()
test = pd.read_excel(path, usecols="H:J", skiprows=1, nrows=9)

result = [x for x in input if isinstance(x, (int, float)) and not pd.isna(x)]
matrix = np.array(result).reshape(-1, 3)
result_df = pd.DataFrame(matrix, columns=["x", "y", "z"])

print(all(result_df == test)) # True
