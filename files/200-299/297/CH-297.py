import pandas as pd
import numpy as np

path = "200-299/297/CH-297 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=6)

def give_triangular(x):
    k = np.ceil((np.sqrt(8 * x + 1) - 1) / 2)
    return k * (k + 1) / 2

t = int(give_triangular(len(input)))
seq = np.repeat(np.arange(1, t + 1), np.arange(1, t + 1))[:len(input)]

input['Group'] = seq
result = input.groupby('Group', as_index=False)['Sales'].sum().rename(columns={'Sales': 'Total Sales'})

print(result.equals(test)) # True
