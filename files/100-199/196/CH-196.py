import pandas as pd
import re

path = "CH-196 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=7)

input['ID.1'] = input['ID'].apply(lambda x: re.sub(r'[0-9]', '', x))
input['ID.2'] = input['ID'].apply(lambda x: int(re.sub(r'[A-Z]', '', x)))
result = input.drop(columns=['ID'])

print(result.equals(test)) # True
