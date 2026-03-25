import pandas as pd
import re

path = "300-399/387/CH-387 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", nrows=10, skiprows=2)
test = pd.read_excel(path, usecols="F", nrows=10, skiprows=2).rename(columns=lambda c: re.sub(r"\.\d+$", "", c))

result = input.copy()
result['ID'] = input['ID'].str.replace(r'(\d+|\D+)(\d+|\D+)', r'\2\1', regex=True)

print(result.equals(test))
## [1] TRUE