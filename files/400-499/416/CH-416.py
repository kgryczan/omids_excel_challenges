import pandas as pd
import numpy as np
from functools import lru_cache

path = "400-499/416/CH-416 Number Series.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)

@lru_cache(maxsize=None)
def is_fibonacci(n):
    a, b = 0, 1
    position = 0
    while a < n:
        a, b = b, a + b
        position += 1
    if a == n:
        return position
    else:
        return np.nan

input['Position'] = input['Fibonacci Number'].apply(is_fibonacci)

print(input["Position"].equals(test['n']))
# True