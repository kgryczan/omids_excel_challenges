import pandas as pd
import numpy as np

path = "200-299/261/CH-261 Custom Grouping .xlsx"
input = pd.read_excel(path, skiprows=1, usecols="B:C", nrows=14)
test = pd.read_excel(path, skiprows=1, usecols="F:H", nrows=14).rename(columns=lambda col: col.replace('.1', ''))

def make_assign_group():
    group = [1]
    seen = set()
    def assign(id_val):
        if id_val in seen:
            group[0] += 1
            seen.clear()
        seen.add(id_val)
        return group[0]
    return assign

result = input.copy()
result['Group'] = result['ID'].apply(make_assign_group())

print(result.equals(test)) # True