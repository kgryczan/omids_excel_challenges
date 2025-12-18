import pandas as pd
import numpy as np

path = "300-399/343/CH-343 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=2, nrows=10)
test = (
    pd.read_excel(path, usecols="F:G", skiprows=2, nrows=4)
    .rename(columns=lambda col: col.replace('.1', ''))
    .sort_values(by=['Sales', 'ID'], ascending=[True, True])
    .reset_index(drop=True)
)
input['ID'] = input['ID'].str[:2]
result = input.groupby('ID', as_index=False).agg({'Sales': 'sum'})

print(result.equals(test)) # True