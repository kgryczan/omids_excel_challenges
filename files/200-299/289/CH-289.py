import numpy as np
import pandas as pd

path = "200-299/289/CH-289 Aggregation.xlsx"
input = pd.read_excel(path, header=None, usecols="B:E", skiprows=2, nrows=7).to_numpy()
test  = pd.read_excel(path, header=None, usecols="G:J", skiprows=2, nrows=7).to_numpy()

def get_neighbour(df, r, c):
    r_rng = slice(max(0, r-1), min(df.shape[0], r+2))
    c_rng = slice(max(0, c-1), min(df.shape[1], c+2))
    vals = df[r_rng, c_rng].copy().astype(float)
    vals[r - max(0, r-1), c - max(0, c-1)] = np.nan
    return np.nanmean(vals)

output = np.array([
    [get_neighbour(input, r, c) for c in range(input.shape[1])]
    for r in range(input.shape[0])
])

print(np.allclose(output, test, equal_nan=True)) # True