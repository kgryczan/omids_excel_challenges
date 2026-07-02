import pandas as pd

path = "400-499/436/CH-436 Number Series.xlsx"
input = pd.read_excel(path, usecols="B", nrows=8, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=8, skiprows=2)


def pell_index(n):
    a, b, i = 0, 1, 0
    while a < n:
        a, b, i = b, 2 * b + a, i + 1
    return float(i) if a == n else float("nan")


result = input.copy()
result["n"] = result["Pell Number"].apply(pell_index)

print(result["n"].equals(test["n"]))
# True
