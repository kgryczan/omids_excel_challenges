import pandas as pd
import numpy as np

path = "300-399/333/CH-333 Pattern Combinations.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="F", skiprows=1, nrows=7)

def shift_column(s, n):
    return np.roll(s.to_numpy(), -n)

input['Column 2'] = shift_column(input['Column 2'], 1)
input['Column 3'] = shift_column(input['Column 3'], 2)
input['Combinations'] = input.astype(str).agg(''.join, axis=1)

print(input['Combinations'].equals(test['Combinations'])) # True