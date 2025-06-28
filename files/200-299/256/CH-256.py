import pandas as pd

path = "200-299/256/CH-256 Table Transformation.xlsx"
input = pd.read_excel(path, usecols="B:H", nrows=5, skiprows=1)
test = pd.read_excel(path, usecols="B:E", nrows=5, skiprows=9)

result = (input.groupby('Date').sum()
    .T.groupby(lambda x: x[0]).sum()
    .T.reset_index())
for col in result.columns:
     if col != 'Date':
          result[col] = result[col].astype(int)

print(result.equals(test)) # True