import pandas as pd

path = "300-399/372/CH-372 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=3)

result = input[input['ID'].astype(str).str.contains(r'[13579]')].reset_index(drop=True)

print(result['ID'].equals(test['ID.1']))
# [1] True