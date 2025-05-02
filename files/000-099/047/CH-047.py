import pandas as pd

input = pd.read_excel("CH-047 Multiple text replaces.xlsx", sheet_name="Sheet1", usecols="B", skiprows=1)
dict = pd.read_excel("CH-047 Multiple text replaces.xlsx", sheet_name="Sheet1", usecols="E:F", skiprows=1).fillna(" ")
test = pd.read_excel("CH-047 Multiple text replaces.xlsx", sheet_name="Sheet1", usecols="J", skiprows=1)
test.columns = input.columns

for index, row in dict.iterrows():
    input["Product IDs"] = input["Product IDs"].str.replace(row[0], row[1])

print(input.equals(test)) # True