import pandas as pd
import re
from math import prod

path = "300-399/382/CH-382 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=6)

def is_valid(s):
    nums = [int(d) for d in re.findall(r"[1-9]", str(s))]
    num_prod = prod(nums)
    num_sum = sum(nums)
    return num_prod % 4 == 0 or num_sum % 3 == 0

result = input[input["ID"].apply(is_valid)].reset_index(drop=True)

print(result["ID"].equals(test.iloc[:, 0]))
# True
