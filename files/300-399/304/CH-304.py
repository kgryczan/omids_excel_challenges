import pandas as pd
import re

path = "300-399/304/CH-304 Reverse Substrings Between Dashes.xlsx"
input = pd.read_excel(path, usecols="B", nrows=6)
test = pd.read_excel(path, usecols="C", nrows=6)

input['Result'] = input.iloc[:, 0].apply(
    lambda s: re.sub(r'(?<=-)\w+(?=-)', lambda m: m.group(0)[::-1], s)
)
print(input['Result'].equals(test['Result'])) # True
