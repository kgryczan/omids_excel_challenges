import pandas as pd

path = "300-399/397/CH-397 Index.xlsx"
input = pd.read_excel(path, usecols="B:F", nrows=21, skiprows=2)
test = pd.read_excel(path, usecols="G", nrows=21, skiprows=2)

r = input.copy()
r["cons"] = r.groupby("Customer")["Product"].transform(
    lambda x: (x != x.shift()).cumsum()
)
r["count"] = r.groupby(["Customer", "cons"])["cons"].transform("count")
r["Mark"] = r["count"].apply(lambda x: "*" if x >= 2 else None)

print(r["Mark"].equals(test["Mark"]))
# True