import pandas as pd
import re

path = "200-299/231/CH-231 Column Splitting.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=6).astype(str)

result = input["ID"].str.extract(r"([a-zA-Z0-9]+)([^a-zA-Z0-9]+)([a-zA-Z0-9]+)")
result.columns = ["Before Symbol", "Symbol", "After Symbol"]

print(test.equals(result))