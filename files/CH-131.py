import pandas as pd

path = "CH-131 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="C:I", skiprows=1, nrows=5).rename(columns=lambda x: x.replace('.1', ''))
test = pd.read_excel(path, usecols="K:N", skiprows=1, nrows=11).rename(columns=lambda x: x.replace('.1', '').replace('.2', ''))

result = pd.concat([input.iloc[:, :4], input.iloc[:, [0, 4, 5, 6]]], axis=0).reset_index(drop=True)

print(result.equals(test))  # True