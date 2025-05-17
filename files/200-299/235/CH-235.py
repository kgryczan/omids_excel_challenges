import pandas as pd

path = "200-299/235/CH-235 Filtering & Removing.xlsx"
input = pd.read_excel(path, usecols="B:F", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="H", skiprows=1, nrows=4).rename(columns=lambda col: col.replace('.1', ''))

input_long = input.melt(id_vars=input.columns[0], value_name="Value")
grouped = input_long.groupby(input.columns[0])["Value"].apply(lambda x: ",".join(map(str, sorted(x, reverse=True))))
result = grouped.drop_duplicates().index.to_frame(index=False)


print(result.equals(test)) # True