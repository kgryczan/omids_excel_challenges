import pandas as pd

path = "200-299/238/CH-238 Consecutive Numbers.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=18)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=18).rename(columns=lambda col: col.replace('.1', ''))
test['Count'] = test['Count'].astype(str)

input.columns = ['Numbers']
g = (input['Numbers'] != input['Numbers'].shift(1) + 1).cumsum()
input['Count'] = input.groupby(g)['Numbers'].transform(lambda x: '-' if len(x)==1 else str(len(x)))
result = input[['Numbers', 'Count']]

print(result == test) # One row is different