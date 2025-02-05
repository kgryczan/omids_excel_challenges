import pandas as pd
import re

path = "CH-185 Replace consecutive X.xlsx"
input = pd.read_excel(path,usecols="C:D", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=9).rename(columns=lambda x: x.split('.')[0])

input['ID'] = [re.sub(r'[Xx]+', 'X', str(x)) for x in input['ID']]

print(input.equals(test))