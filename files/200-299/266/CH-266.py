import pandas as pd

path = "200-299/266/CH-266 Extract from Text.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=6)

def find_repeating_pattern(s):
    n = len(s)
    for l in range(1, n // 2 + 1):
        unit = s[:l]
        times = n // l
        repeated = unit * times
        if s.startswith(repeated[:n]):
            return unit
    return s

input['Pattern'] = input['Text'].apply(find_repeating_pattern)

print(input["Pattern"].equals(test['Pattern'])) # True