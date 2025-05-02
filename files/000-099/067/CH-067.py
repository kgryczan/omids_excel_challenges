import pandas as pd

input = pd.read_excel("CH-067 Index Selections.xlsx", usecols="B:H", skiprows= 1, nrows = 15)
test  = pd.read_excel("CH-067 Index Selections.xlsx", usecols="J", skiprows=1, nrows = 5)

result = input[(input.iloc[:, 1:6] <= 7).sum(axis=1) >= 2].iloc[:,0].reset_index(drop=True)

print(result.tolist() == test.iloc[:,0].tolist()) # True
