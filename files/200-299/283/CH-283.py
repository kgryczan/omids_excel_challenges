import pandas as pd

path = "200-299/283/CH-283 Advanced Sorting.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=7)
test.columns = input.columns

result = input.loc[
    input.drop("Product ID", axis=1)
      .apply(lambda r: (-r.nlargest(2)).tolist(), axis=1)
      .argsort()
].reset_index(drop=True)

print(result.equals(test)) # True