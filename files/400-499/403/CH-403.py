import pandas as pd

path = "400-499/403/CH-403 Number Puzzles - Happy Numbers.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)

def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

input['Is Happy?'] = input['Number'].apply(is_happy)

print(input['Is Happy?'].equals(test['Is Happy?']))