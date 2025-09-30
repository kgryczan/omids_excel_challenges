import pandas as pd
import numpy as np

path = "300-399/303/CH-303 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=5)

def rotate_until_non_na(x):
    x = list(x)
    if all(pd.isna(x)): return x
    i = next(idx for idx, val in enumerate(x) if not pd.isna(val))
    return x[i:] + x[:i]

rotated = input.apply(rotate_until_non_na, axis=0)
rotated = rotated.dropna(how='all')
rotated = rotated.iloc[1:].reset_index(drop=True)
rotated.columns = input.apply(rotate_until_non_na, axis=0).iloc[0]
if 'Date' in rotated.columns:
    rotated['Date'] = pd.to_datetime(rotated['Date'])
rotated.columns.name = None

rotated = rotated.replace(np.nan, '', regex=True)
test = test.replace(np.nan, '', regex=True)

print(rotated.equals(test)) # True