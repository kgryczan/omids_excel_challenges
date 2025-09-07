import pandas as pd

path = "200-299/292/CH-292 Advanced Filtering.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="G", skiprows=1, nrows=4)

result = input[input.drop('ID', axis=1).apply(lambda row: len(set(row)) == len(row), axis=1)][['ID']].reset_index(drop=True)

print(result['ID'].equals(test['Selected IDs'])) # True