import pandas as pd
from collections import Counter

path = "300-399/348/CH-348 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=3).rename(columns=lambda col: col.replace('.1', ''))

def has_char_at_least_3(s):
    counts = Counter(str(s))
    return any(v >= 3 for v in counts.values())

result = input[input['ID'].apply(has_char_at_least_3)].reset_index(drop=True)

print(result.equals(test)) # True