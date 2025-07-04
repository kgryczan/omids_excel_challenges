import pandas as pd
import re
from itertools import islice

path = "200-299/259/CH-259 Extract from Text.xlsx"
input = pd.read_excel(path, usecols="B", nrows=2, skiprows=1).iloc[0, 0]
test = pd.read_excel(path, usecols="D", nrows=2, skiprows=1).iloc[0, 0]

pattern = r"[A-Z][a-z][0-9]-[0-9]{2}[A-Z][a-z]"
windows = [
    ''.join(islice(input, i, i + 8))
    for i in range(len(input) - 7)
]
matches = ', '.join([window for window in windows if re.search(pattern, window)])

print(matches == test) # True
