import pandas as pd
path = "300-399/309/CH-309 Advanced Filtering.xlsx"
df = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=4).rename(columns=lambda col: col.replace('.1', ''))

result = df[df.Sales == df.Sales.rolling(3, center=True).max()].dropna().reset_index(drop=True)
print(result.equals(test))
