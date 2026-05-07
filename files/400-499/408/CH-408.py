import pandas as pd

path = "400-499/408/CH-408 Number Puzzles - Self Number.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)

def self_number(n):
    s = n
    for c in str(n):
        s += int(c)
    return s
def is_self_number(n):
    for i in range(n):
        if self_number(i) == n:
            return False
    return True

result = input['Number'].apply(is_self_number)
print(result == test['Is Self Number?'])
# Incorrect testing output.