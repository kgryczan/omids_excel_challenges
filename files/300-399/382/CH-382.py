import pandas as pd
import re
from math import prod

path = "300-399/382/CH-382 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=7)

def is_valid(s):
    nums = [int(d) for d in re.findall(r"[1-9]", str(s))]
    num_prod = prod(nums)
    return num_prod % 4 == 0 or num_prod % 3 == 0

result = input[input["ID"].apply(is_valid)].reset_index(drop=True)

print(result["ID"].equals(test.iloc[:, 0]))
# PQ1347 which is filtered out shouldn't be because product is 105 which is divisible by 3.
