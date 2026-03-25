import numpy as np
import pandas as pd

input_data = pd.read_excel("CH-019 Suduku in Excel.xlsx", usecols="B:G", skiprows=2, nrows=6, header=None).apply(pd.to_numeric)
test = pd.read_excel("CH-019 Suduku in Excel.xlsx", usecols="O:T", skiprows=2, nrows=6, header=None)

grid = input_data.to_numpy(dtype=float)

def fill_single_missing_rows_cols(arr):
    changed = True
    while changed:
        changed = False
        for i in range(arr.shape[0]):
            mask = np.isnan(arr[i])
            if mask.sum() == 1:
                arr[i, np.where(mask)[0][0]] = 21 - np.nansum(arr[i])
                changed = True
        for j in range(arr.shape[1]):
            mask = np.isnan(arr[:, j])
            if mask.sum() == 1:
                arr[np.where(mask)[0][0], j] = 21 - np.nansum(arr[:, j])
                changed = True
    return arr

grid = fill_single_missing_rows_cols(grid)
missing = np.argwhere(np.isnan(grid))
if len(missing) == 2:
    rows = np.unique(missing[:, 0])
    cols = np.unique(missing[:, 1])
    first_row = set(range(1, 7)) - set(grid[rows[0], ~np.isnan(grid[rows[0]])].astype(int))
    second_row = set(range(1, 7)) - set(grid[rows[1], ~np.isnan(grid[rows[1]])].astype(int))
    first_col = set(range(1, 7)) - set(grid[~np.isnan(grid[:, cols[0]]), cols[0]].astype(int))
    second_col = set(range(1, 7)) - set(grid[~np.isnan(grid[:, cols[1]]), cols[1]].astype(int))
    grid[rows[0], cols[0]] = list(first_row & first_col)[0]
    grid[rows[1], cols[1]] = list(second_row & second_col)[0]
grid = fill_single_missing_rows_cols(grid)

print(np.array_equal(grid, test.to_numpy()))
