import pandas as pd

path = "400-499/404/CH-404 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=7, skiprows=2).rename(columns=lambda c: c.rstrip(".1") if c.endswith(".1") else c)

result = input.copy()
result["Product ID"] = result["Product ID"].str.replace(
	r"^((?:[^X]*X){2}[^X]*)X",
	r"\1-",
	regex=True,
)

print(result.equals(test))
# fourth entry incorrect in test. 