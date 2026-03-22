import pandas as pd

path = "300-399/385/CH-385 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=2, nrows=7)
test  = pd.read_excel(path, usecols="G:J", skiprows=2, nrows=7).rename(columns=lambda c: __import__("re").sub(r"\.\d+$", "", c))

result = input.copy()
mask = result["Date"] >= pd.Timestamp("2024-08-14")
result.loc[mask, "Customer ID"] = result.loc[mask, "Customer ID"].str.replace("X", "C", n=1)

print((result == test).all().all())
## Output: True