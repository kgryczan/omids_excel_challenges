import pandas as pd
import numpy as np

path = "200-299/233/CH-233 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=100)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=9)

def compute_range_table(x):
    x = np.sort(np.ravel(x))
    x = x[~np.isnan(x)]
    n = len(x)
    rows = []
    for pct in range(10, 100, 10):
        k = int(np.ceil(pct / 100 * n))
        i = np.argmin(x[k-1:] - x[:n-k+1])
        rows.append({'%': pct / 100, 'Range': f"{int(x[i])}-{int(x[i+k-1])}"})
    return pd.DataFrame(rows)

result = compute_range_table(input.values)

print(result.equals(test))