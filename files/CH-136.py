import pandas as pd
from itertools import groupby

# Read the Excel file
path = "CH-136 Column Splitting.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=7, dtype=str).fillna("")

def separate_by_double(string):
    split_data = [string[0]]
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            split_data[-1] += ","
        split_data.append(string[i])
    split_data = ''.join(split_data).split(",")
    return split_data + [""] * (3 - len(split_data))

result = pd.DataFrame([separate_by_double(id) for id in input.iloc[:, 0]], columns=["ID.1", "ID.2", "ID.3"])

print(result.equals(test)) # Output: True