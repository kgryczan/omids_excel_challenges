import pandas as pd

path = "400-499/413/CH-413 Number Puzzles - Happy Number.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)

def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

for i, row in input.iterrows():
    n = row[0]
    result = is_happy(n)
    expected = test.iloc[i, 0]
    print(f"Input: {n}, Output: {result}, Expected: {expected}, {'PASS' if result == expected else 'FAIL'}")

result = expected
# # all results are happy. wrong expected values