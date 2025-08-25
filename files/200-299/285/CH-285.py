import pandas as pd
from itertools import combinations

path = "200-299/285/CH-285 Text Matching.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=10)\
    .sort_values(['ID 1', 'ID 2']).reset_index(drop=True)

def score(a, b):
    a, b = a.replace("-", ""), b.replace("-", "")
    m1 = sum(ch in a for ch in list(b))
    m2 = sum(ch in b for ch in list(a))
    return max(m1, m2)

pairs = [(i, j) for i, j in combinations(input["ID"], 2) if score(i, j) >= 3]
result = pd.DataFrame(pairs, columns=["ID 1", "ID 2"])\
    .sort_values(["ID 1", "ID 2"]).reset_index(drop=True)

print(result.equals(test)) # True