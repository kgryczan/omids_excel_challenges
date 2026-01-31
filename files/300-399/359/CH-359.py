import pandas as pd

path = "300-399/359/CH-359 Replacement.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="G:J", skiprows=2, nrows=8).rename(columns=lambda col: col.replace(".1", ""))

input["Customer ID"] = input["Customer ID"].where(input["Customer ID"].map(input["Customer ID"].value_counts()) != 1, "Other")

print(input.equals(test))
# True