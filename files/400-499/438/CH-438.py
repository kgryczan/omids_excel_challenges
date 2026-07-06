import pandas as pd
import math

path = "400-499/438/CH-438 Number Puzzles - Spy Number.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)

result = [
    n
    for n in range(10000, 20001)
    if sum(int(x) for x in str(n)) == math.prod(int(x) for x in str(n))
][:7]
