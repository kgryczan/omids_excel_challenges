import pandas as pd
import re

input = pd.read_excel("CH-045 Text Split.xlsx", usecols="B", skiprows=1)
test = pd.read_excel("CH-045 Text Split.xlsx", usecols="D:H", skiprows=1)


split_text = input['ID'].str.extractall(r'(\D+|\d+)')
split_text = split_text.unstack().droplevel(0, axis=1)
split_text.columns = test.columns
split_text['Part 2'] = split_text['Part 2'].astype('int64')
split_text['Part 4'] = split_text['Part 4'].astype('float64')

print(split_text.equals(test)) # True