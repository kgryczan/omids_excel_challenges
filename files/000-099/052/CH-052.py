import pandas as pd

input = pd.read_excel("CH-052 Find missing Numbers.xlsx",  usecols="B", skiprows=1)
test = pd.read_excel("CH-052 Find missing Numbers.xlsx",  usecols="J", skiprows=1, nrows = 5)

missing = list(set(range(min(input["Input"]), max(input["Input"]) + 1)) - set(input["Input"]))

print(missing == test["Missing Numbers"].tolist()) # True