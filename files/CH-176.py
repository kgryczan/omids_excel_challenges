import pandas as pd

path = "CH-176 Custom Grouping.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=26)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=5).rename(columns=lambda x: x.split('.')[0])

input['Group'] = (input.index // 5) + 1
result = input.drop(columns=['Date']).groupby('Group').sum()
result.reset_index(inplace=True)

print(result.equals(test)) # True