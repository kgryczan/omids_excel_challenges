import pandas as pd
import re

path = "CH-191Column Splitting.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=6).astype(str)

input[['Part 1', 'Separator', 'Part 2']] = input.iloc[:, 0].str.extract(r"([A-Za-z0-9]+)([^A-Za-z0-9])(.*)").astype(str)
result = input[['Part 1', 'Separator', 'Part 2']]
print(result.equals(test))  # True