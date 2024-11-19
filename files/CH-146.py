import pandas as pd
import numpy as np

path = "CH-146 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=7)

input[['ID.1', 'ID.2', 'ID.3']] = input['ID'].str.split('|', expand=True)

input[['ID.1', 'ID.2', 'ID.3']] = input[['ID.1', 'ID.2', 'ID.3']].apply(lambda col: col.fillna(pd.NA))
input['ID.2'] = input.apply(lambda row: np.NaN if pd.isna(row['ID.2']) else f"{row['ID.1']}{row['ID.2']}", axis=1)
input['ID.3'] = input.apply(lambda row: np.NaN if pd.isna(row['ID.3']) else f"{row['ID.2']}{row['ID.3']}", axis=1)
input = input.drop(columns=['ID'])

print(input.equals(test))   # True