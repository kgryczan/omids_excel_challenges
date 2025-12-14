import pandas as pd

path = "300-399\\341\\CH-341 Filter.xlsx"
input = pd.read_excel(path, usecols="B", nrows = 8, skiprows = 2)
test = pd.read_excel(path, usecols="F", nrows=3, skiprows=2).rename(columns=lambda c: c.replace('.1', ''))

filtered = input[input["ID"].str.contains(r"N.*M", na=False)].reset_index(drop=True)

print(filtered.equals(test)) # True