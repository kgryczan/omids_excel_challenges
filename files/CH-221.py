import pandas as pd
import re

path = "CH-221 Combining the columns.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="E", skiprows=1, nrows=6).rename(columns=lambda col: col.replace('.1', ''))

input_data['Text'] = input_data['Text'].str.replace(r'[a-z]', '', regex=True)

print(input_data.equals(test)) # True