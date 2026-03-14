import pandas as pd
import re

path = "300-399/381/CH-381 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=7)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=4)

def is_valid(num):
    digits = [int(d) for d in re.findall(r"\d", str(num))]
    parities = [d % 2 for d in digits]
    diffs = [abs(parities[i + 1] - parities[i]) for i in range(len(parities) - 1)]
    return sum(diffs) >= 2

result = input[input["ID"].apply(is_valid)].reset_index(drop=True)

print(result["ID"].equals(test["ID.1"]))
# [1] TRUE
