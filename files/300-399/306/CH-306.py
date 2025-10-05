import pandas as pd
from itertools import combinations

path = "300-399/306/CH-306 Increasing Pair Sum Finder.xlsx"
input = pd.read_excel(path, usecols="B", nrows=10)
test = pd.read_excel(path, usecols="E", nrows=10)

ids = range(1, len(input) + 1)
vals = input['Question'].values

pairs = [(a, b) for a, b in combinations(ids, 2) if vals[a-1] < vals[b-1] and vals[a-1] + vals[b-1] >= 12]
result = pd.DataFrame([f"{vals[a-1]},{vals[b-1]}" for a, b in pairs], columns=['Result'])

print(result.equals(test)) # True