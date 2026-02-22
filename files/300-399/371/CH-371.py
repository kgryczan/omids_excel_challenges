import pandas as pd
import re

path = "300-399/371/CH-371 Text Cleaning.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=2, nrows=6)
test = pd.read_excel(path, usecols="E", skiprows=2, nrows=6)

def remove_wrapped(s):
    pattern = re.compile(r'(.)[^\\1]*?\1')
    while pattern.search(s):
        s = pattern.sub('', s)
    return s

result = input['ID'].apply(remove_wrapped)
print(result.equals(test['ID.1']))
# Output: True