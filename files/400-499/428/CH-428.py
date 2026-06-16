import pandas as pd

path = "400-499/428/CH-428 Number Puzzles - Self Number.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)


def digit_sum(n):
    return sum(map(int, str(n)))


def nearest_self(x):
    limit = x + 9 * len(str(x))
    generated = {n + digit_sum(n) for n in range(1, limit + 1)}
    self_numbers = [n for n in range(1, limit + 1) if n not in generated]

    return min(self_numbers, key=lambda n: (abs(n - x), n))


result = [nearest_self(x) for x in input.iloc[:, 0]]
# different results
