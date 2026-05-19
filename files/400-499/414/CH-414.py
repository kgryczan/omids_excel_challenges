import pandas as pd

path = "400-499/414/CH-414 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=7, skiprows=2).rename(columns=lambda c: c.replace('.1', ''))

result = input.copy()
result['Product ID'] = result['Product ID'].str.replace(r'X(\d)', r'X-\1', regex=True)

print(result.equals(test))
# True