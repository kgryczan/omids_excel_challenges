import pandas as pd

path = "400-499/422/CH-422 Matrix Normalization.xlsx"
input = pd.read_excel(path, usecols="C:F", nrows=4, skiprows=3, header=None)
test = pd.read_excel(path, usecols="J:M", nrows=4, skiprows=3, header=None)

result = input.subtract(input.to_numpy()[:, ::-1].diagonal(), axis=0)
result.columns = test.columns

print(result.equals(test))
#> True