import pandas as pd
import re

path = "CH-175 Remove consecutive X.xlsx"

input = pd.read_excel(path, usecols="C:D", skiprows=1, nrows=9)
test = pd.read_excel(path, usecols="G", skiprows=1, nrows=9).fillna("").rename(columns=lambda x: x.split('.')[0])

input['ID'] = input['ID'].apply(lambda x: re.sub(r'[xX]{2,}', '', x))

print(input[['ID']].equals(test)) # True