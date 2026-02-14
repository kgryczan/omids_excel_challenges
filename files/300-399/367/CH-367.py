import pandas as pd
import re

path = "300-399/367/CH-367 Text Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", nrows = 7, skiprows = 2)
test = pd.read_excel(path, usecols="E", nrows=7, skiprows=2).rename(columns=lambda x: x.replace(".1", ""))

input['ID'] = input['ID'].apply(lambda x: re.sub(r'(.+)\1+', r'\1', x))

print(input.equals(test))
# True