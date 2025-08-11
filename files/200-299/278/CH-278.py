import pandas as pd
from itertools import groupby

path = "200-299/278/CH-278 Pattern Recognition.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=6, skiprows=1)
test = pd.read_excel(path, usecols="D", nrows=6, skiprows=1)

input['Pattern Length'] = input['Pattern'].apply(lambda s: len([k for k,_ in groupby(s)]) - 1)

print(input["Pattern Length"].equals(test['Pattern Length'])) # True