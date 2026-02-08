import pandas as pd
from itertools import combinations

path = "300-399/364/CH-364 Custom Grouping.xlsx"
df = pd.read_excel(path, usecols="B:C", skiprows=2, nrows=6)
test = pd.read_excel(path, usecols="F:G", skiprows=2, nrows=5)

prices = df['Price'].tolist()

input_combinations = []
for r in range(2, len(prices) + 1):
    for comb in combinations(range(len(prices)), r):
        s = sum(prices[i] for i in comb if pd.notna(prices[i]))
        if s in {10, 13}:
            letters = ",".join(chr(65 + i) for i in comb)
            input_combinations.append(letters)

input_combinations.sort()

# Note: One combination in the test table is incorrect. It should be ACDE, not ABDE (ABDE sum is 12).