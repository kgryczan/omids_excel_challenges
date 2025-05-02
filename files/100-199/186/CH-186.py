import pandas as pd
import numpy as np

path = "CH-186 Column Splitting.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=7).fillna("").astype('str')

input['ID.1'] = input['ID'].str.replace(r'[^aeiouAEIOU]', '', regex=True)
input['ID.2'] = input['ID'].str.replace(r'[aeiouAEIOU]', '', regex=True)
result = input.drop(columns=['ID'])

print(result.equals(test)) # True