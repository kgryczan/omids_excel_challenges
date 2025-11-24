import pandas as pd
import numpy as np

path = "300-399/331/CH-331 Pattern Combinations.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="E", skiprows=1, nrows=2).iloc[:, 0].tolist()

p1_str = "".join(np.where(input.index % 2 == 0, input.iloc[:, 0], input.iloc[:, 1]).astype(str))
p2_str = "".join(np.where(input.index % 2 == 0, input.iloc[:, 1], input.iloc[:, 0]).astype(str))

result = [p1_str, p2_str]
print(result == test) # True