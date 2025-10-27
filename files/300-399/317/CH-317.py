import pandas as pd
import numpy as np

input_path = "300-399/317/CH-317 Custom Grouping.xlsx"
input = pd.read_excel(input_path, usecols="B:C", skiprows=1, nrows=18)
test = pd.read_excel(input_path, usecols="G:H", skiprows=1, nrows=5)

result = input.assign(Group=(np.floor(np.log2(np.arange(1, len(input)+1)))+1).astype(int))\
    .groupby('Group', as_index=False)['Sales'].sum().rename(columns={'Sales': 'Total Sales'})

print(result.equals(test)) # True