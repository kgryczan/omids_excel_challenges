import pandas as pd

path = "400-499/419/CH-419 Filter.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=5, skiprows=2)
test = pd.read_excel(path, usecols="G:H", nrows=2, skiprows=2)
test.columns = input.columns


result = input[input['Sales'] > input.groupby('Product')['Sales'].transform('mean')].reset_index(drop=True)
print(result.equals(test))
# [1] True