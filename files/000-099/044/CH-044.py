import pandas as pd

input1 = pd.read_excel("CH-044 Combine Tables.xlsx", usecols = "C:F", nrows = 4, skiprows=2)
input2 = pd.read_excel("CH-044 Combine Tables.xlsx", usecols="C:G", skiprows = 8, nrows = 4)
input3 = pd.read_excel("CH-044 Combine Tables.xlsx", usecols="C:F", skiprows = 14, nrows = 4)
test = pd.read_excel("CH-044 Combine Tables.xlsx", usecols="J:O", skiprows = 1, nrows = 5)

input1 = input1.melt(id_vars="Regions")
input2 = input2.melt(id_vars="Regions")
input3 = input3.melt(id_vars="Regions")
result = pd.concat([input1, input2, input3])
result = result.groupby(["Regions", "variable"]).sum().reset_index()
result = result.pivot(index="Regions", columns="variable", values="value").reset_index().fillna(0)
result[result.columns[1:]] = result[result.columns[1:]].astype('int64')
result.columns.name = None

print(result.equals(test)) # True