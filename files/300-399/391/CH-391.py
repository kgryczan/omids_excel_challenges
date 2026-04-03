import pandas as pd

path = "300-399/391/CH-391 Index.xlsx"
input = pd.read_excel(path, usecols="B:F", nrows=21, skiprows=2)
test = pd.read_excel(path, usecols="G", nrows=21, skiprows=2)

input['Mark'] = input.groupby('Customer').cumcount().apply(lambda x: '*' if x == 0 else None)

print(input['Mark'].equals(test['Mark']))
# [1] True