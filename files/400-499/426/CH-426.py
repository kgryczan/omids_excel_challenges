import pandas as pd
from functools import lru_cache

path = "400-499/426/CH-426 Number Series.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)


def find_nth_term(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * find_nth_term(n - 1) + find_nth_term(n - 2)


find_nth_term = lru_cache(maxsize=None)(find_nth_term)
input["Term"] = input["n"].apply(find_nth_term)
print(input["Term"].equals(test["Pell  Number"]))
# True
