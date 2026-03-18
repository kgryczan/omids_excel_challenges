import pandas as pd

path = "300-399/383/CH-383 Filter.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="F", skiprows=2, nrows=2)

def is_valid(s):
    digits = [c for c in str(s) if c.isdigit()]
    return int(digits[0]) % 2 == 0 and int(digits[-1]) % 2 == 1

result = input[input["ID"].apply(is_valid)].reset_index(drop=True)

print(result["ID"].equals(test["ID.1"]))
# True
