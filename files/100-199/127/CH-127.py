import pandas as pd
import itertools

path = "CH-127 Add Index Column.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=12)
test = pd.read_excel(path, usecols="E:G", skiprows=1, nrows=12).rename(columns=lambda x: x.replace('.1', ''))

input = input.sort_values(by='Stock')
input["index"] = input.groupby(['Stock', (input.groupby('Stock')['Price'].diff() < 0).cumsum()]).cumcount() + 1

print(input.equals(test)) # True