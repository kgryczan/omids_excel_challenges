import pandas as pd
from itertools import product

path = "300-399/374/CH-374 Text Cleaning.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=6)
test = pd.read_excel(path, usecols="E", skiprows=2, nrows=6).rename(columns=lambda x: x.replace('.1', ''))
test['ID'] = test['ID'].fillna("")

def bounded_substrings(s):
    chars = list(s)
    n = len(chars)
    
    substrings = []
    for i, j in product(range(n - 1), range(1, n)):
        if i < j and chars[i] == chars[j]:
            substrings.append(''.join(chars[i + 1:j]))
    
    return substrings

input['substrings'] = input['ID'].apply(lambda x: ', '.join(bounded_substrings(x)))
print(input['substrings'].equals(test['ID']))
# > True